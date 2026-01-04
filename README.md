# Pharmacy Operations Backend (Django)

## Overview
This project is a Django-based backend system designed to manage internal pharmacy operations.
It mirrors real-world enterprise systems used by large pharmacy chains for inventory and order management.

The system is **admin-driven**, focuses on **data integrity**, and exposes **secure APIs** for internal or app-based consumption.
There is no frontend UI by design.

---

## Key Features

- Role-based access control
- Multi-store support
- Inventory management (Medicine, Batch, Stock)
- Order lifecycle management
- Transaction-safe stock updates
- Auditability and admin safety
- Clean REST APIs using Django REST Framework

---

## Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- SQLite (development)
- Django Admin

---

## Project Structure
pharmacy_backend/
├── users/
├── stores/
├── inventory/
├── orders/
├── products/
├── pharmacy_backend/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── manage.py


---

## Core Modules

### Users & Roles
- Extends Django User with business roles
- Store-linked users
- Role-based data visibility
- Permissions enforced at admin and API level

---

### Stores
- Multi-store architecture
- Manager assignment
- Active/inactive store control
- Admin-managed lifecycle

---

### Inventory
- Medicine master data
- Batch-level tracking (expiry, MRP)
- Store-wise stock management
- Inventory updates only via confirmed orders

---

### Orders
- Order and OrderItem modeling
- Order lifecycle: CREATED → CONFIRMED → CANCELLED
- Atomic transactions for stock deduction
- Confirmed orders are protected from deletion

---

## Security & Auditability

- Authentication-protected APIs
- Role-based access control
- Audit fields (`created_by`, `created_at`, `updated_at`)
- Read-only system fields in admin
- Restricted destructive actions in admin

---

## Django Admin Usage

Django Admin is used as an **internal operations console**:
- Inline editing for related data
- Search, filters, and ordering
- Audit visibility
- Safe admin workflows

---

## API Capabilities (Sample)

- List stores
- View inventory by store
- Create and manage orders
- Role-restricted write operations

APIs are designed for **internal systems or mobile apps**, not public exposure.

---

## How to Run Locally

### 1. Setup virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

