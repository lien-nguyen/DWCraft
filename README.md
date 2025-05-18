# DWCraft

**DWCraft** is a Django-based project designed to support the development of a professional course platform. 

> ⚠️ This project is currently in development.

## 🚀 Project Vision
- Build and learn by doing: this project documents a solo journey into developing, deploying, and managing a course platform from scratch.
- Explore best practices in Django development, open-source tooling, CI/CD workflows, and content management.
- Serve as a foundation for future educational products and business initiatives.

## 🔧 Tech Stack
- Python 3.12
- Django 5.x
- PostgreSQL 15
- Docker + Docker Compose
- Markdown for course modules and blog posts
- GitHub Actions for CI
- TailwindCSS (or Bootstrap)

## 📂 Project Structure (to be extended)
```
dwhcraft/
├── Dockerfile
│   ├── core
│   ├── docker-compose.yml
│   ├── dwh_course
│   ├── manage.py
│   ├── requirements.txt
│   ├── static
│   │   ├── css
│   │   └── img
│   └── templates
```

## 📖 Part of the Build2Teach Initiative
This codebase is part of the larger `Build2Teach` project, which aims to offer high-quality, self-hosted online courses and empower independent course creators.

## 🧪 Local Development
```bash
cp .env.example .env
docker-compose up --build
python manage.py migrate
python manage.py createsuperuser
```

## 🔒 License
This is a **private, non-distributed** project. All rights reserved.

For personal use only — not licensed for public distribution or contribution.
