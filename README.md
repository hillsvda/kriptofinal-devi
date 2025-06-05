# Kriptografi

![Ekran görüntüsü 2025-06-05 185309](https://github.com/user-attachments/assets/e8b92b20-64f8-4cb7-9d0f-b8029b186daf)


##  Özellikler

### AES Şifreleme
- Metin şifreleme ve çözme
- Otomatik anahtar ve IV üretimi
- Şifreli metin, anahtar ve IV kopyalama
  
  ![Ekran görüntüsü 2025-06-05 185319](https://github.com/user-attachments/assets/14d811fb-0200-44fd-bd80-f95aabde5130)


### RSA Şifreleme
- Metin şifreleme ve çözme
- Otomatik anahtar çifti üretimi (Public/Private Key)
- Küçük dosya şifreleme desteği (.txt, .pdf, .docx, max 10KB)
- Şifreli dosya indirme
- Anahtarları kopyalama
![Ekran görüntüsü 2025-06-05 185336](https://github.com/user-attachments/assets/144fee2a-8f80-4b47-86cc-0c4bac8b13a6)
![Ekran görüntüsü 2025-06-05 185357](https://github.com/user-attachments/assets/71bdda2b-4792-45b0-bf56-c34a15f3eba5)
![Ekran görüntüsü 2025-06-05 185447](https://github.com/user-attachments/assets/b32a8261-0e13-450e-98e9-5d8d6823c9de)

### SHA256 Özet
- Metin özetleme
- Dosya özetleme (sürükle-bırak desteği)
- Büyük harfli özet gösterimi
- Özet kopyalama
![Ekran görüntüsü 2025-06-05 185246](https://github.com/user-attachments/assets/d8fe29a0-96a1-455d-96a2-fd1865b7ae3b)
![Ekran görüntüsü 2025-06-05 190726](https://github.com/user-attachments/assets/70cae964-498e-4fa3-8f26-1d602717b09b)

##  Arayüz Özellikleri
- Neon efektli butonlar ve kartlar
- Responsive tasarım
- Sürükle-bırak dosya yükleme
- Modern ve kullanıcı dostu arayüz

##  Teknolojiler
- Flask (Backend)
- Bootstrap 5 (Frontend)
- Font Awesome (İkonlar)
- Crypto.js (Şifreleme)
- Modern JavaScript (ES6+)

##  Kurulum
1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```
2. Uygulamayı başlatın:
```bash
python app.py
```
3. Tarayıcınızda açın:
```
http://127.0.0.1:5000
```

##  Gereksinimler
- Python 3.7+
- Flask
- pycryptodome
- cryptography
