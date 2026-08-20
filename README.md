# 🥛 Milk Man Backend

Backend API for the **Milk Man App**, designed to manage customers, milkmen, daily milk deliveries, payments, and transaction history.

The system supports two separate applications:

* 📱 **Customer App** — View milk deliveries, payments, and history.
* 🚚 **Milkman App** — Mark deliveries, update quantities, and manage customers.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │      Customer App   │
                    └──────────┬──────────┘
                               │
                               │ REST API
                               ▼
                    ┌─────────────────────┐
                    │    Milk Man Backend │
                    │      (FastAPI)      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Database       │
                    └─────────────────────┘
                               ▲
                               │
                               │ REST API
                    ┌──────────┴──────────┐
                    │     Milkman App     │
                    └─────────────────────┘
```

Both applications use the same backend API while having different user experiences and permissions.

---

## 🎯 Main Responsibilities

The backend handles:

* User management
* Milkman management
* Customer–milkman relationships
* Daily milk delivery records
* Milk quantity tracking
* Payment records
* Transaction history
* Authentication and authorization
* API validation
* Database operations

---

# 🗄️ Database Design

The backend is divided into separate tables based on responsibility.

## 1. Users Table

Stores customer information.

| Column       | Description           |
| ------------ | --------------------- |
| `id`         | Unique user ID        |
| `name`       | Customer name         |
| `phone`      | Customer phone number |
| `address`    | Customer address      |
| `milkman_id` | Assigned milkman      |

### Example

```text
users
-------------------------
id
name
phone
address
milkman_id
```

---

## 2. Milkmen Table

Stores milkman information.

| Column    | Description               |
| --------- | ------------------------- |
| `id`      | Unique milkman ID         |
| `name`    | Milkman name              |
| `phone`   | Milkman phone number      |
| `address` | Milkman address           |
| `...`     | Other milkman information |

### Example

```text
milkmen
-------------------------
id
name
phone
address
```

---

## 3. Deliveries Table

Stores the actual daily milk delivery.

Delivery and payment are intentionally separated because they represent two different business operations.

| Column       | Description     |
| ------------ | --------------- |
| `id`         | Delivery ID     |
| `user_id`    | Customer        |
| `milkman_id` | Milkman         |
| `date`       | Delivery date   |
| `quantity`   | Milk quantity   |
| `status`     | Delivery status |
| `created_at` | Creation time   |

### Example

```text
deliveries
-------------------------
id
user_id
milkman_id
date
quantity
status
created_at
```

Possible delivery statuses:

```text
pending
delivered
skipped
cancelled
```

---

# 💰 Payments Table

Stores payment information separately from delivery information.

| Column           | Description    |
| ---------------- | -------------- |
| `id`             | Payment ID     |
| `user_id`        | Customer       |
| `milkman_id`     | Milkman        |
| `amount`         | Payment amount |
| `payment_date`   | Payment date   |
| `status`         | Payment status |
| `payment_method` | Payment method |
| `created_at`     | Creation time  |

### Example

```text
payments
-------------------------
id
user_id
milkman_id
amount
payment_date
status
payment_method
created_at
```

Possible payment methods:

```text
cash
upi
bank_transfer
```

Possible payment statuses:

```text
pending
completed
failed
```

---

# 🔗 Database Relationships

```text
Milkman
   │
   ├───────────────┐
   │               │
   ▼               ▼
Users          Deliveries
   │               │
   │               │
   └───────┬───────┘
           │
           ▼
        Payments
```

### Relationships

```text
Milkman 1 ──── N Users

User 1 ──── N Deliveries

Milkman 1 ──── N Deliveries

User 1 ──── N Payments

Milkman 1 ──── N Payments
```

---

# 🚀 Technology Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **Pydantic**
* **MySQL / PostgreSQL**
* **JWT Authentication**
* **Uvicorn**
* **Alembic** for database migrations

---

# 📁 Project Structure

```text
milk-man-backend/
│
├── app/
│   ├── main.py
│   │
│   ├── database/
│   │   └── database.py
│   │   
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── milkman.py
│   │   ├── delivery.py
│   │   └── payment.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── milkman.py
│   │   ├── delivery.py
│   │   └── payment.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── milkmen.py
│   │   ├── deliveries.py
│   │   └── payments.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── delivery_service.py
│   │   └── payment_service.py
│   │
│   └── core/
│       ├── config.py
│       └── security.py
│
├── migrations/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🔐 Authentication

The backend uses **JWT-based authentication**.

Authentication flow:

```text
Login
  │
  ▼
Backend validates credentials
  │
  ▼
JWT Access Token
  │
  ▼
Client stores token
  │
  ▼
Client sends token with API requests
```

Example header:

```http
Authorization: Bearer <access_token>
```

Different roles can be supported:

```text
CUSTOMER
MILKMAN
ADMIN
```

---

# 📡 API Structure

## Authentication

```http
POST /auth/register
POST /auth/login
POST /auth/refresh-token
```

---

## Users

```http
GET    /users/me
GET    /users/{user_id}
PUT    /users/{user_id}
```

---

## Milkmen

```http
GET    /milkmen/me
GET    /milkmen/{milkman_id}
GET    /milkmen/{milkman_id}/customers
```

---

## Deliveries

```http
POST   /deliveries
GET    /deliveries
GET    /deliveries/{delivery_id}
PUT    /deliveries/{delivery_id}
```

Example:

```json
{
    "user_id": 101,
    "milkman_id": 10,
    "quantity": 1.0,
    "date": "2026-08-20"
}
```

---

## Payments

```http
POST   /payments
GET    /payments
GET    /payments/{payment_id}
```

Example:

```json
{
    "user_id": 101,
    "milkman_id": 10,
    "amount": 500,
    "payment_method": "upi"
}
```

---

# 🥛 Milk Delivery Flow

```text
Customer places/has daily milk requirement
                │
                ▼
          Milkman App
                │
                ▼
       Scan Customer QR
                │
                ▼
       Identify Customer
                │
                ▼
       Confirm Quantity
                │
                ▼
       Create Delivery
                │
                ▼
          Database
```

If the customer requests a different quantity:

```text
Default Quantity
      │
      ▼
Milkman changes quantity
      │
      ▼
Updated Delivery Record
```

Example:

```text
Normal quantity: 1 L

Customer requests: 0.5 L

Delivery:
quantity = 0.5
```

---

# 💳 Payment Flow

Payment is independent from delivery.

```text
Daily Deliveries
       │
       ▼
Calculate total
       │
       ▼
Customer payment
       │
       ▼
Payment record
       │
       ▼
Payment history
```

This separation makes it possible to support:

* Daily deliveries
* Monthly billing
* Partial payments
* Multiple payments
* Payment history
* Outstanding balances

without modifying delivery records.

---

# 📊 Example Monthly Calculation

Suppose:

```text
Milk price = ₹50 / litre

Day 1  → 1 L
Day 2  → 1 L
Day 3  → 0.5 L
Day 4  → 1 L
```

Total:

```text
3.5 L × ₹50
= ₹175
```

The delivery records remain unchanged even after payment.

Payment:

```text
Amount = ₹175
Status = completed
```

---

# ⚙️ Environment Variables

Create a `.env` file:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/milkman

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

Never commit `.env` to Git.

---

# 🛠️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd milk-man-backend
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment

Create:

```text
.env
```

and add the required database and JWT configuration.

## 5. Run Server

```bash
uvicorn app.main:app --reload
```

Backend will be available at:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically provides API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🧪 Testing

Run tests using:

```bash
pytest
```

Example:

```text
tests/
├── test_auth.py
├── test_users.py
├── test_deliveries.py
└── test_payments.py
```

---

# 🔒 Security

The backend should:

* Hash passwords before storing them.
* Never store plain-text passwords.
* Validate JWT tokens.
* Validate request data using Pydantic.
* Apply role-based authorization.
* Keep secrets inside environment variables.
* Validate ownership before modifying records.
* Use HTTPS in production.

---

# 🌐 Production Architecture

```text
                 Customer App
                      │
                      │
                      ▼
                ┌───────────┐
                │   HTTPS   │
                └─────┬─────┘
                      │
                      ▼
                ┌───────────┐
                │  FastAPI  │
                │  Backend  │
                └─────┬─────┘
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
        Application         Database
           Logic          MySQL/PostgreSQL
```

---

# 🔮 Future Improvements

Possible future features:

* QR-based customer identification
* Automatic monthly billing
* UPI payment integration
* Payment reminders
* Delivery notifications
* Push notifications
* Admin dashboard
* Milk price management
* Multiple milk types
* Subscription management
* Delivery analytics
* Customer and milkman reports

---

# 📌 Design Principles

The backend follows these principles:

1. **Separate delivery and payment responsibilities.**
2. **Keep the customer and milkman applications separate at the UI level.**
3. **Use one centralized backend and database.**
4. **Use role-based authentication.**
5. **Keep business logic inside services rather than API routes.**
6. **Use database relationships instead of duplicating data.**
7. **Maintain a complete history of deliveries and payments.**

---

# 👨‍💻 Project Status

🚧 **Currently under development**

The backend architecture and database design are being developed for the Milk Man application.
