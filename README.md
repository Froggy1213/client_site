# Rafik Ammar — Personal Website

A professional personal website for Rafik Ammar, a Global Policy Director. The site is designed with a "Modern Intellectual" aesthetic: minimalist layout, authoritative typography, and a monochrome palette with subtle gold accents to convey expertise and trust.

## 📋 Key Features

* **Homepage:** Static biographical information, professional experience trajectory, and core competencies (hardcoded for precise layout control).
* **Library (Publications):** A dynamic section for books and reports, fully manageable via the database.
* **Admin Panel:** Easy management of book entries, cover images, and external purchase links via Django Admin.
* **Responsive Design:** Fully optimized for mobile and desktop devices.
* **Custom Design:** Built with clean HTML5/CSS3 (Grid & Flexbox) using Inter and Playfair Display fonts (no heavy CSS frameworks).

## 🛠 Tech Stack

* **Backend:** Python 3.10+, Django 5.x
* **Database:** SQLite (Lightweight and efficient for personal portfolios)
* **Media Handling:** Pillow (Image processing)
* **Frontend:** HTML5, CSS3
* **Deployment:** PythonAnywhere

## 🚀 Local Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Froggy1213/client_site.git](https://github.com/Froggy1213/client_site.git)
    cd client_site
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Linux/Mac
    python3.10 -m venv .venv
    source .venv/bin/activate

    # Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (to access the Admin panel):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    The site will be available at: `http://127.0.0.1:8000/`

## 🌍 Deployment (PythonAnywhere)

This project is configured for deployment on PythonAnywhere.

**Brief Deployment Steps:**
1.  **Clone:** Pull the code into a Bash console.
2.  **Virtualenv:** Create a virtualenv and install `requirements.txt`.
3.  **Static Files:** Run `python manage.py collectstatic` to gather CSS/JS.
4.  **Web App:** Configure the WSGI file to point to `raf_site.settings`.
5.  **Mappings:** Set Static files mapping (`/static/` -> `staticfiles` folder).

## 📂 Project Structure

* `raf_site/` — Core Django settings and main URL routing.
* `portfolio/` — The main application logic.
    * `models.py` — Database models for Books and Purchase Links.
    * `templates/` — HTML templates (`base.html`, `index.html`, `books.html`).
    * `static/` — CSS files and static assets (e.g., profile photo).
* `media/` — Directory for user-uploaded content (book covers).
* `manage.py` — Django command-line utility.

---
**Status:** Live 🟢