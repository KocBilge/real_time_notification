# Real-Time Notification System

Bu proje, kullanıcıların gerçek zamanlı bildirimler almasını sağlayan bir sistemdir. FastAPI, Celery ve Pydantic kullanılarak geliştirilmiştir. Kullanıcılar, belirli olaylar gerçekleştiğinde bildirimler alabilir ve bildirim geçmişini görüntüleyebilir.

## Özellikler

- Gerçek zamanlı bildirim gönderimi
- WebSocket desteği ile anlık güncellemeler
- Kullanıcı yönetimi (kayıt ve profil görüntüleme)
- Bildirim türleri ve kategorileri
- Bildirim geçmişi görüntüleme

## Teknolojiler

- **FastAPI**: Hızlı ve modern bir web çerçevesi.
- **Celery**: Asenkron görevler için arka plan işlem yönetimi.
- **Pydantic**: Veri doğrulama ve ayarları için.
- **Redis**: Celery için broker ve backend olarak kullanılır.
- **WebSocket**: Gerçek zamanlı güncellemeler için.

## Kurulum

### Gereksinimler

- Python 3.7+
- Redis (Celery broker olarak kullanılacak)

### Sanal Ortamın Oluşturulması ve Paketlerin Yüklenmesi

1. Projeyi klonlayın:
    ```bash
    git clone https://github.com/KocBilge/real_time_notification.git
    cd real_time_notification
    ```

2. Sanal ortam oluşturun ve aktif edin:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

### Redis'in Başlatılması

Redis'i başlatın (eğer Redis yüklü değilse, [Redis kurulum talimatlarına](https://redis.io/download) göz atabilirsiniz):
```bash
redis-server

API Kullanımı

Kullanıcı Kaydı: POST /register/
Gövde: { "username": "string", "email": "string", "password": "string" }
Yanıt: { "message": "User registered" }
Kullanıcı Profili: GET /profile/{user_id}
Yanıt: { "user_id": "integer" }
Bildirim Gönderimi: POST /notify/
Gövde: { "user_id": "integer", "message": "string", "category": "string" }
Yanıt: { "message": "Notification sent" }
Bildirim Geçmişi: GET /history/{user_id}
Yanıt: { "user_id": "integer", "notifications": [...] }
