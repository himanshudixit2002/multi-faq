# Multi-Language FAQ System

## Installation
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Usage
```bash
curl http://localhost:8000/api/faqs/
curl http://localhost:8000/api/faqs/?lang=hi
curl http://localhost:8000/api/faqs/?lang=bn
```

## Docker Support
```bash
docker-compose up --build