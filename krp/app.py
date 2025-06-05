from flask import Flask, render_template, request, jsonify, send_file
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib
import os
import tempfile

app = Flask(__name__)

def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt_aes(iv, ct, key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = base64.b64encode(key.export_key()).decode('utf-8')
    public_key = base64.b64encode(key.publickey().export_key()).decode('utf-8')
    return private_key, public_key

def encrypt_rsa(data, public_key_b64):
    public_key = RSA.import_key(base64.b64decode(public_key_b64))
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(data.encode())
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_rsa(encrypted_b64, private_key_b64):
    private_key = RSA.import_key(base64.b64decode(private_key_b64))
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_b64))
    return decrypted.decode('utf-8')

def calculate_sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aes')
def aes_page():
    return render_template('aes.html')

@app.route('/rsa')
def rsa_page():
    return render_template('rsa.html')

@app.route('/encrypt_aes', methods=['POST'])
def encrypt_aes_route():
    data = request.json['data']
    key = get_random_bytes(32)  # 256-bit key
    iv, encrypted_data = encrypt_aes(data, key)
    return jsonify({
        'encrypted_data': encrypted_data,
        'iv': iv,
        'key': base64.b64encode(key).decode('utf-8')
    })

@app.route('/decrypt_aes', methods=['POST'])
def decrypt_aes_route():
    data = request.json
    key = base64.b64decode(data['key'])
    decrypted_data = decrypt_aes(data['iv'], data['encrypted_data'], key)
    return jsonify({'decrypted_data': decrypted_data})

@app.route('/encrypt_rsa', methods=['POST'])
def encrypt_rsa_route():
    data = request.json['data']
    private_key, public_key = generate_rsa_keys()
    encrypted_data = encrypt_rsa(data, public_key)
    return jsonify({
        'encrypted_data': encrypted_data,
        'private_key': private_key,
        'public_key': public_key
    })

@app.route('/decrypt_rsa', methods=['POST'])
def decrypt_rsa_route():
    data = request.json
    decrypted_data = decrypt_rsa(data['encrypted_data'], data['private_key'])
    return jsonify({'decrypted_data': decrypted_data})

@app.route('/generate_rsa_keys', methods=['POST'])
def generate_rsa_keys_route():
    private_key, public_key = generate_rsa_keys()
    return jsonify({
        'private_key': private_key,
        'public_key': public_key
    })

@app.route('/hash', methods=['POST'])
def hash():
    data = request.json['data']
    hash_value = calculate_sha256(data)
    return jsonify({'hash': hash_value})

@app.route('/encrypt_rsa_file', methods=['POST'])
def encrypt_rsa_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Dosya bulunamadı'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Dosya seçilmedi'}), 400
    # Sadece küçük dosyalar için kontrol
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    if size > 10240:
        return jsonify({'error': 'Dosya boyutu çok büyük. (Maksimum 10KB)'}), 400
    data = file.read()
    # Anahtar üret
    private_key, public_key = generate_rsa_keys()
    public_key_obj = RSA.import_key(base64.b64decode(public_key))
    cipher = PKCS1_OAEP.new(public_key_obj)
    # Dosya parça parça şifrelenir (her parça 190 byte)
    encrypted = b''
    chunk_size = 190
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        encrypted += cipher.encrypt(chunk)
    # Geçici dosyaya yaz
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.enc')
    temp.write(encrypted)
    temp.close()
    # Anahtarları da döndür
    return send_file(temp.name, as_attachment=True, download_name=file.filename + '.enc'), 200, {
        'X-Public-Key': public_key,
        'X-Private-Key': private_key
    }

if __name__ == '__main__':
    app.run(debug=True) 