# 🐾 Flask URL Shortener

Welcome to your tiny corner of the internet where long URLs go to get a glow-up ✨  
This is a lightweight, no-nonsense URL shortener built with Flask—perfect for turning monstrous links into sleek, shareable ones.

[![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-blue)](https://flask.palletsprojects.com/)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://www.python.org/)  
[![Tailwind Ready](https://img.shields.io/badge/Styled%20with-Bootstrap-AA55FA)](https://getbootstrap.com/)

---

## 🌟 Features

- 🔗 Shorten any valid URL with a single click  
- 🧠 Smart redirection using unique short codes  
- 🎨 Simple, customizable UI (ready for Bootstrap magic)  
- 🐍 Built with Python and Flask—minimal dependencies, maximum charm  
- 📦 Easily extendable for analytics, QR codes, or user accounts  

---

## 🚀 Getting Started

Clone the repo and get cozy:
```bash
git clone https://github.com/shreekanthkapparagaon/FLASK-URL-shortener.git
cd FLASK-URL-shortener
```

Create and activate a virtual environment:
```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

Install dependencies:
```cmd
pip install -r requirement.txt
```

Run the app:
```bash
python main.py
```
Visit http://localhost:5000 and start shortening!


---
## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** Flask
- **Templating:** Jinja2
- **Database:** SQLite (or swap in any relational DB)
- **Styling:** Bootstrap 5
- **Runtime:** Works locally or on any WSGI-friendly host

---


## 🤝 Contributing

Contributions make this project better—for everyone.

1. **Fork** the repository
2. **Create a feature branch:**  
   ```bash
   git checkout -b feature/awesome-feature
   git commit -m "Add awesome feature"
   git push origin feature/awesome-feature
   ```

---

## 🗺️ Roadmap

- [ ] Dark mode toggle (Bootstrap utility classes)
- [ ] QR code generation for short links
- [ ] Click analytics dashboard (views, referrers, timestamps)
- [ ] Rate limiting and spam protection
- [ ] User accounts with custom slugs and link management
- [ ] Dockerfile and CI workflow


---
##  💬 Final words

Built with ❤️ by [Shreekanth](https://github.com/shreekanthkapparagaon).  
Because every long URL deserves a second chance.  
Enjoy, customize, and happy shortening! 🚀