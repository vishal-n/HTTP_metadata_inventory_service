# 📦 HTTP Metadata Inventory Service

A high-performance backend service that collects and inventories HTTP metadata (headers, cookies, and page source) for any given URL.

Built using:

* **Python 3.11**
* **FastAPI**
* **MongoDB**
* **Docker Compose**
* **Async Background Processing**
* **Pytest**

---

# 🚀 Features

✅ Create metadata records for any URL
✅ Retrieve metadata instantly if available
✅ Async background metadata collection on cache miss
✅ Non-blocking API responses
✅ MongoDB indexed storage
✅ Fully containerized environment
✅ Separation of Concerns (API / Service / Repository)
✅ Ready for horizontal scaling

---

# 🧠 System Design Overview

The service follows a layered architecture:

```
Client
  |
FastAPI (Transport Layer)
  |
Service Layer (Business Logic)
  |
Repository Layer (MongoDB)
  |
Async Metadata Worker (httpx)
```

---

## 📌 GET Endpoint Workflow

| Scenario              | Behaviour                        |
| --------------------- | -------------------------------- |
| Metadata exists in DB | Returns 200 OK immediately       |
| Metadata missing      | Returns 202 Accepted immediately |
| Background task       | Fetches metadata asynchronously  |
| Next GET              | Returns stored metadata          |

The metadata collection:

* runs asynchronously
* does not block request-response cycle
* avoids internal HTTP self-calls
* persists results for future retrieval

---

# 📁 Project Structure

```
metadata-inventory/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   ├── repository/
│   ├── services/
│   ├── worker/
│   └── api/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```
git clone git@github.com:vishal-n/HTTP_metadata_inventory_service.git
cd metadata-inventory
```

---

## 2️⃣ Run Using Docker Compose (Mandatory)

Start API and MongoDB:

```
docker-compose up --build
```

---

## 3️⃣ API Documentation

Swagger UI available at:

```
http://localhost:8000/docs
```

---

# 📡 API Endpoints

---

## 🔹 POST `/metadata`

Collect metadata for a given URL.

### Request Body

```
{
  "url": "https://example.com"
}
```

### Response

```
{
  "message": "Metadata collected"
}
```

---

## 🔹 GET `/metadata`

Retrieve metadata for a given URL.

### Query Param

```
/metadata?url=https://example.com
```

---

### Case 1: Metadata Exists

```
200 OK
{
  url,
  headers,
  cookies,
  page_source
}
```

---

### Case 2: Metadata Missing

```
202 Accepted
{
  "message": "Metadata collection initiated"
}
```

Background metadata collection starts automatically.

---

# 🗄 Database Design

Collection: `metadata`

```
{
  url: string,
  headers: object,
  cookies: object,
  page_source: string
}
```

Indexed Field:

```
url (unique)
```

Ensures:

* fast lookups
* no duplicate records
* scalability with dataset growth

---

# 🧪 Running Tests

```
pytest
```

---

# 🛠 Configuration

Environment variables:

```
MONGO_URI=mongodb://mongo:27017
DB_NAME=metadata_db
```

---