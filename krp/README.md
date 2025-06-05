# Kripto Operasyon Merkezi

Bu uygulama, AES şifreleme ve SHA256 özet fonksiyonlarını içeren criminal temalı bir web uygulamasıdır.

## Özellikler

- AES şifreleme ve şifre çözme
- SHA256 özet oluşturma
- Criminal temalı modern arayüz
- Güvenli anahtar yönetimi

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Uygulamayı çalıştırın:
```bash
python app.py
```

3. Tarayıcınızda `http://localhost:5000` adresine gidin.

## Kullanım

1. AES Şifreleme:
   - Metni girin ve "Şifrele" butonuna tıklayın
   - Şifreli metin, IV ve anahtar bilgilerini kaydedin

2. AES Şifre Çözme:
   - Şifreli metni, IV ve anahtarı girin
   - "Şifre Çöz" butonuna tıklayın

3. SHA256 Özet:
   - Metni girin ve "Özet Oluştur" butonuna tıklayın
   - SHA256 özet değerini alın

## Güvenlik Notları

- Anahtarları güvenli bir şekilde saklayın
- Hassas verileri şifrelerken güçlü anahtarlar kullanın
- Şifreli verileri güvenli bir şekilde iletin 