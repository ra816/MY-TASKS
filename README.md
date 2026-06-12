# ✅ TaskFlow – Premium Todo App (Django Full Stack Python)

A feature-rich, multi-user Todo Management web application built with **Django**, featuring authentication, priorities, categories, due dates, and a modern responsive UI.

## 🚀 Features
- 🔐 **User Authentication** – Register, Login, Logout (each user sees only their own tasks)
- 🗂️ **Categories** – Create custom categories with color labels (Work, Personal, Study, etc.)
- ⭐ **Priority Levels** – High / Medium / Low, color-coded
- 📅 **Due Date & Time** – Set deadlines; overdue tasks are highlighted
- 🔍 **Search & Filters** – Filter by status, priority, category, or search by keyword
- 📊 **Dashboard Stats** – Total, Pending, and Completed task counters
- ✅ **Full CRUD** – Add, edit, complete/undo, delete tasks
- 🎨 **Modern UI** – Clean gradient design with Bootstrap 5 + custom CSS
- 🛠️ **Admin Panel** – Manage all users' tasks and categories

## 🛠️ Tech Stack
- **Backend:** Python, Django (MVT architecture)
- **Frontend:** HTML, CSS (custom), Bootstrap 5
- **Database:** SQLite
- **Auth:** Django built-in authentication system

## 📂 Project Structure
```
todo_django_v2/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── todos/
    ├── models.py          # Todo & Category models
    ├── forms.py           # Auth, Todo, Category forms
    ├── views.py           # Auth + CRUD + filtering logic
    ├── urls.py
    ├── admin.py
    ├── migrations/
    ├── templates/todos/
    │   ├── base.html
    │   ├── login.html
    │   ├── register.html
    │   ├── todo_list.html
    │   ├── todo_form.html
    │   ├── todo_confirm_delete.html
    │   ├── category_list.html
    │   └── category_confirm_delete.html
    └── static/css/
        └── style.css
```

## ⚙️ Setup Instructions

1. **Extract the project and open terminal inside it**
   ```bash
   cd todo_django_v2
   ```

2. **Create & activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **(Optional) Create admin/superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Open browser → `http://127.0.0.1:8000/`
   - Register a new account → start adding tasks!
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📌 Application Routes
| URL                     | Description                  |
|--------------------------|-------------------------------|
| `/register/`            | Create a new account          |
| `/login/`                | User login                    |
| `/logout/`               | User logout                   |
| `/`                      | Dashboard – list all tasks    |
| `/add/`                  | Add new task                  |
| `/edit/<id>/`            | Edit a task                   |
| `/delete/<id>/`          | Delete a task                 |
| `/toggle/<id>/`          | Mark complete/incomplete      |
| `/categories/`           | Manage categories             |
| `/categories/delete/<id>/`| Delete a category            |
| `/admin/`                | Django admin panel            |

## 📖 Project Overview

### Problem Statement
Generic todo apps lack personalization — users need a way to organize tasks by category and priority, set deadlines, and track personal progress securely.

### Methodology / Approach
- Designed `Todo` and `Category` models linked to Django's `User` model (one-to-many relationships).
- Implemented Django's built-in authentication system for secure registration/login/logout.
- Built dynamic filtering (status, priority, category, search) using Django QuerySets.
- Designed a responsive, modern UI using Bootstrap 5 with a custom gradient theme and color-coded priority/category badges.
- Added overdue detection using Django's timezone utilities.

### Results / Outcome
A fully functional multi-user Todo web application with secure login, categorized & prioritized task management, due-date tracking, filtering/search, and a real-time dashboard summary.

### Conclusion
This project demonstrates a complete full-stack Python web application using Django's MVT architecture, covering authentication, relational database design (ForeignKey relationships), form handling, and responsive frontend design — core skills for full-stack Python development.

## 👨‍💻 Author
CRT 2027 Batch – Mini Project Submission
