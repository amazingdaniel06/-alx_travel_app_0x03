# Celery Configuration
CELERY_BROKER_URL = "amqp://localhost"   # RabbitMQ default
CELERY_RESULT_BACKEND = "rpc://"

# Email Backend (example using console, replace with SMTP in production)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_password"
DEFAULT_FROM_EMAIL = "Booking <your_email@gmail.com>"
