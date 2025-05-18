# DWCraft

**DWCraft** is an open-source project that demonstrates how to build a modern data warehouse course platform from scratch — using Django, Docker, PostgreSQL, and markdown-based course content. This project forms the technical backbone of the `Build2Teach` learning platform.

> ⚠️ **Work in Progress**: This repository is currently under private development (pre-release). Expect rapid changes, incomplete features, and evolving structure. The project will be made public once a minimal working version is stable.

## 🚀 Project Goals
- Develop a self-hosted platform for delivering structured, high-quality online courses
- Use open source tools exclusively (no commercial BI tools)
- Showcase end-to-end CI/CD integration
- Align with DevOps and reproducible data architecture principles

## 🔧 Tech Stack
- Python 3.12
- Django 5.x
- PostgreSQL 15
- Docker + Docker Compose
- Markdown for course modules and blog posts
- GitHub Actions for CI
- TailwindCSS (or Bootstrap)

## 📂 Repo Structure
```
dwhcraft/
├── build2teach/          # Django project folder
├── course/               # App for course modules
├── blog/                 # App for blog posts
├── core/                 # App for homepage/about/contact
├── users/                # Auth, newsletter, registration
├── static/               # Images, CSS, JS
├── templates/            # HTML templates
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── manage.py
```

## 📖 Powered by `Build2Teach`
This codebase supports the instructional project and upcoming book:

> **Build2Teach: From Dev to Production with Django and Open Source**

For more info, visit [coming soon](https://build2teach.com) 🚧

## 🧪 Local Development
```bash
cp .env.example .env
docker-compose up --build
python manage.py migrate
python manage.py createsuperuser
```

## 🛠 Contributing
Coming soon! This project will welcome contributors once the MVP is finalized.

## License
MIT License — free to use, modify, and teach from.
