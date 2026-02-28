
# 🌾 ALX Backend Capstone – Farm Orders Management System

## 📌 Project Overview

The **Farm Orders Management System** is a full-stack Django web application designed to manage agricultural product listings and customer orders.

It allows:

* Users to register and log in
* Farmers/vendors to add products
* Customers to browse available products
* Customers to place and manage orders
* Administrators to manage the system through the Django admin panel
* Developers to interact with the backend via REST API endpoints

This project combines:

* 🌐 **Django Templates (UI Layer)**
* 🔐 **Authentication System**
* 🧠 **Django REST Framework (API Layer)**
* 🗄 **Relational Database Models**
* 🛒 Product & Order Management Logic**

---

# 🎯 Project Objectives

The system was built to demonstrate:

* Backend architecture design
* RESTful API development
* Authentication and authorization
* Database modeling with relationships
* Separation of concerns (UI vs API)
* Full project structuring for scalability

---

# 🏗 System Architecture

The project follows a layered architecture:

```
Client (Browser)
       │
       ▼
Django Template Views (HTML UI)
       │
       ▼
Business Logic (Views & Forms)
       │
       ▼
Models (Database Layer)
       │
       ▼
SQLite Database
```

Additionally:

```
External Clients
       │
       ▼
REST API Endpoints (/api/)
       │
       ▼
Django REST Framework
```

---

# 🧩 Project Structure

```
ALX_BE_Capstone/
│
├── accounts/        # User authentication & profile management
├── products/        # Product management
├── orders/          # Order processing system
├── farm_orders/     # Main project configuration
├── core/            # Shared utilities (if applicable)
├── templates/       # HTML templates
├── static/          # CSS/JS files
├── media/           # Uploaded files
└── manage.py
```

---

# 🔐 Authentication System (accounts app)

## Features

* User Registration
* Login & Logout
* User Dashboard
* Profile Management
* JWT Authentication (API)

## UI Routes

```
/accounts/register/
/accounts/login/
/accounts/dashboard/
/accounts/logout/
```

## API Routes

```
/api/auth/register/
/api/auth/login/
/api/auth/profile/
```

---

# 🛍 Product Management (products app)

## Features

* Create products
* View product list
* API-based product CRUD
* Admin product management

## UI Routes

```
/products/
/products/create/
```

## API Routes

```
/api/products/
/api/products/<id>/
```

---

# 🧾 Order Management (orders app)

## Features

* Create orders
* View personal orders
* Link orders to authenticated user
* API order management

## UI Routes

```
/orders/
/orders/create/
```

## API Routes

```
/api/orders/
/api/orders/<id>/
```

---

# 🗄 Database Design

## User Model

* Username
* Email
* Password
* Role (if extended)
* Profile details

## Product Model

* Name
* Description
* Price
* Quantity
* Created by (User)

## Order Model

* User (ForeignKey)
* Product (ForeignKey)
* Quantity
* Order date
* Status

### Relationships

* One User → Many Products
* One User → Many Orders
* One Product → Many Orders

---

# 🔄 How It Works (User Flow)

## 1️⃣ User Registration

1. User visits `/accounts/register/`
2. Fills form
3. Account created
4. Automatically logged in
5. Redirected to dashboard

---

## 2️⃣ Adding Products

1. Authenticated user visits `/products/create/`
2. Submits product details
3. Product saved to database
4. Appears in product list

---

## 3️⃣ Ordering a Product

1. User browses `/products/`
2. Selects product
3. Creates order via `/orders/create/`
4. Order linked to logged-in user
5. Order visible in `/orders/`

---

# 🌐 API Usage

The project also exposes REST endpoints for integration.

Example:

```
GET /api/products/
POST /api/products/
GET /api/orders/
POST /api/orders/
```

Authentication uses:

* JWT tokens
* Session authentication (for browser)

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/SimonMuriu-cpu/ALX_BE_Capstone.git
cd ALX_BE_Capstone
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

## 6️⃣ Run Server

```bash
python manage.py runserver
```

---

# 🧪 Testing the Application

### Admin Panel

```
http://127.0.0.1:8000/admin/
```

### UI Pages

```
http://127.0.0.1:8000/accounts/register/
http://127.0.0.1:8000/products/
http://127.0.0.1:8000/orders/
```

### API

```
http://127.0.0.1:8000/api/products/
```

---

# 🔒 Security Features

* CSRF Protection
* Login Required Decorators
* JWT Authentication
* Session-based authentication
* Password hashing (Django default)

---

# 📦 Technologies Used

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite
* HTML Templates
* Bootstrap (if used)
* Git & GitHub

---

# 🚀 Future Improvements

* Payment integration
* Role-based permissions (Farmer vs Customer)
* Product categories
* Order tracking status updates
* Email notifications
* Deployment to cloud (Heroku / Render / AWS)

---

# 🧠 Key Learning Outcomes

This project demonstrates:

* Django project structuring
* API + Template hybrid architecture
* Model relationships
* Authentication systems
* RESTful design
* URL routing and modular design
* Debugging and error resolution

---
