# 🚀 Hangarin: Task and To-Do Manager

## 📌 Description

**Hangarin** is a web-based task management platform designed to streamline organization, enhance productivity, and provide users with data-driven insights into their workflow. It enables efficient tracking of tasks, subtasks, and notes within a structured and user-friendly environment.

---

## ✨ Features

### 📊 Dashboard Overview
- Displays summary cards showing task distribution across categories and priorities  
- Provides analytical insights into user productivity  

### 🔄 Full CRUD Functionality
- Create, read, update, and delete:
  - Tasks  
  - Subtasks  
  - Notes  
- Supports flexible task management across any timeframe  

### 🔍 Accessibility Tools
- Search, filter, and sorting options  
- Pagination for handling large datasets  
- Intuitive navigation for improved usability  

### 🧩 Inline Subtasks and Notes
- Add subtasks and notes directly during task creation  
- Streamlines the data entry process  

### 📱 Responsive Design
- Fully optimized for mobile and small-screen devices  
- Ensures accessibility across different screen sizes  

### 🔐 Google Authentication
- Secure login using Google accounts  
- Simplifies user authentication process  

---

## 🗂️ Data Models

| Model     | Description |
|----------|------------|
| Category | Classifies tasks based on their context or environment |
| Priority | Defines the importance level of tasks |
| Task     | Core model containing primary task details |
| Subtask  | Smaller components of a task providing additional structure |
| Notes    | Comments and reminders associated with a task |

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2.12  
- **Frontend:** Bootstrap  
- **Database:** SQLite  
- **Libraries & Tools:**  
  - django-widget-tweaks (form customization)  
  - Faker (sample data generation)  
  - django-extra-views (inline form handling)  

---

## ⚙️ Installation Guide

### 1️⃣ Create and Activate Virtual Environment

python -m venv <environment_name>
# Windows
Scripts\activate
# macOS/Linux
source bin/activate

### 2️⃣ Clone the Repository

git clone https://github.com/FernandezCorporate/Hangarin_Task-To-do_Manager.git
cd PSUSphere

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Apply Migrations

cd projectsite  
python manage.py makemigrations  
python manage.py migrate  

### 5️⃣ Create Superuser

python manage.py createsuperuser

### 6️⃣ Run the Development Server

python manage.py runserver

---

## 🚧 Initial Setup

- Access the Django admin panel at http://127.0.0.1:8000/admin/  
- Create initial records for:
  - Categories  
  - Priorities  
- On CLI, navigate to projectsite folder and run: python manage.py create_initial_data
- Run development server again and access login at http://127.0.0.1:8000/
- Click google icon and login using your google account  
- Also, this web application is also hosted at : [pythonanywhere](https://hagarinapp.pythonanywhere.com)

---

## 📈 Future Improvements (Optional Ideas)

- Task deadlines and reminders  
- Email or push notifications  
- Data visualization charts for productivity trends  
- REST API integration for external access  

---

## 👨‍💻 Author

**Name:** Allen Glenn Flojemon Fernandez  
**Course:** BS Information Technology - 3rd Year (Block 2)  
**Email:** allenglennfernandez04@gmail.com  
**Github:** https://github.com/FernandezCorporate


