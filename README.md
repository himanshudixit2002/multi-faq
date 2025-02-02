# Multi-Language FAQ System 🔍

![Django Version](https://img.shields.io/badge/django-5.1-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.12-blue)

A comprehensive FAQ system with multilingual support powered by Django and Redis.

## Features ✨
- 🌐 WYSIWYG editor integration (CKEditor)
- 🔄 Automatic translation caching with Redis
- 🌍 Multi-language API endpoints
- 📦 Docker-ready configuration
- 📊 Admin dashboard with rich text editing

## Quick Start 🚀

```bash
# Clone repository
git clone https://github.com/yourusername/multi-faq.git
cd multi-faq

# Setup virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## API Documentation 📚

### Endpoints
```http
GET /api/faqs/          # Get all FAQs (default English)
GET /api/faqs/?lang=hi  # Get Hindi translations
GET /api/faqs/?lang=bn  # Get Bengali translations
```

### Example Usage
```bash
# Get English FAQs
curl http://localhost:8000/api/faqs/

# Get Hindi translations
curl http://localhost:8000/api/faqs/?lang=hi

# Get Bengali translations
curl http://localhost:8000/api/faqs/?lang=bn
```

## Docker Deployment 🐳
```bash
# Build and start containers
docker-compose up --build

# Access containers
docker exec -it multi-faq-web-1 bash
```

## Configuration ⚙️
1. Create `.env` file:
```ini
DEBUG=True
SECRET_KEY=your-secret-key
REDIS_URL=redis://redis:6379/0
```

## Troubleshooting 🔧
```bash
# Fix port conflicts
sudo lsof -t -i tcp:8000 | xargs kill -9

# Reset migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

## Contributing 🤝
1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open pull request

## License 📄
MIT License - see [LICENSE](LICENSE) for details

---
📧 Contact: [your.email@example.com](mailto:your.email@example.com) | 💬 [Join our Discord](https://discord.gg/your-invite-link)