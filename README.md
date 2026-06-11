# 🎫 Datastraw Support CRM
### A Full-Stack Customer Support Ticketing System

> Built as part of the Datastraw Technologies Internship Assignment — a real, production-ready CRM system deployed and running on live servers.

![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?style=for-the-badge&logo=sqlite)
![TailwindCSS](https://img.shields.io/badge/Tailwind-CSS-38bdf8?style=for-the-badge&logo=tailwindcss)
![Railway](https://img.shields.io/badge/Deployed-Railway-purple?style=for-the-badge)

---

## 🌐 Live Demo

🔗 **[View Live App →](https://datastraw-crm.up.railway.app)**
💻 **[GitHub Repository →](https://github.com/MalayJoshi1/customer-support-ticket-crm-datastraw)**

---

## 🚀 What Is This?

A fully functional **Customer Support Ticketing CRM** that allows support teams to:

- Create and track customer support tickets with auto-generated IDs
- Search and filter tickets in real time across multiple fields
- Update ticket status and add timestamped internal audit notes
- View detailed ticket history and complete audit logs
- Export full ticket transcripts as downloadable files

This is not a toy project — it runs on actual servers with a real database and a REST API.

---

## ✨ Features

### Core Features
| Feature | Description |
|--------|-------------|
| 🎫 **Create Tickets** | Create tickets with customer name, email, subject, and description. Auto-generates unique Ticket ID (TKT-1001) and timestamp. |
| 📋 **List All Tickets** | Clean dashboard view showing ID, customer, subject, status, and filing date. |
| 🔍 **Real-Time Search** | Debounced search across ticket ID, customer name, subject, and description simultaneously. |
| 🔽 **Filter by Status** | Filter tickets by Open, In Progress, or Closed with live counts in the dropdown. |
| 📝 **View & Update Tickets** | Full detail view with status transitions and internal notes/comments system. |

### Bonus Features
| Feature | Description |
|--------|-------------|
| 🌙 **Dark Mode** | Full dark/light mode with system preference detection and localStorage persistence. |
| 📊 **Stats Dashboard** | Live analytics cards showing Total, Open, In Progress, and Closed ticket counts. |
| 📥 **Export Transcript** | Download a full ticket audit log as a `.txt` file including all notes and timestamps. |
| 🔔 **Toast Notifications** | Real-time success/error feedback on all user actions. |
| 📱 **Mobile Responsive** | Fully responsive UI — table view on desktop, card view on mobile. |

---

## 🛠️ Tech Stack

| Layer | Technology | Reason |
|-------|-----------|--------|
| **Backend** | Python + FastAPI | Fast, modern, auto docs, type validation |
| **Database** | SQLite + SQLAlchemy ORM | Simple, serverless, no setup required |
| **Validation** | Pydantic v2 | Strict input/output schema validation |
| **Frontend** | HTML5 |
| **Styling** | Tailwind CSS (CDN) | Utility-first, responsive out of the box |
| **Deployment** | Railway.app | Simple GitHub-connected deployment |

---

## 📁 Project Structure

```
customer-support-ticket-crm-datastraw/
├── frontend/
│   └── index.html           # Full SPA — all HTML, CSS, JS in one file
├── main.py                  # FastAPI app, API routes, CORS, static files
├── models.py                # SQLAlchemy ORM models (Ticket, Note)
├── schemas.py               # Pydantic request/response schemas
├── database.py              # DB engine, session, base config
├── requirements.txt         # Python dependencies         
├── .python-version          # Python version pin for Railway
└── README.md
```

---

## 🗄️ Database Schema

### Tickets Table
| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Primary key, auto-increment |
| `ticket_id` | String | Unique ID e.g. TKT-1001 |
| `customer_name` | String | Customer full name |
| `customer_email` | String | Customer email address |
| `subject` | String | Issue subject/headline |
| `description` | Text | Full issue description |
| `status` | String | Open / In Progress / Closed |
| `created_at` | DateTime | Auto-generated on creation |
| `updated_at` | DateTime | Auto-updated on every change |

### Notes Table
| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Primary key, auto-increment |
| `ticket_id` | String | Foreign key → tickets.ticket_id |
| `note_text` | Text | Internal comment/audit note |
| `created_at` | DateTime | Auto-generated timestamp |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/tickets` | Create a new support ticket |
| `GET` | `/api/tickets` | List all tickets — supports `?status=Open` and `?search=keyword` |
| `GET` | `/api/tickets/{ticket_id}` | Get full ticket detail including all notes |
| `PUT` | `/api/tickets/{ticket_id}` | Update ticket status and optionally add a note |
| `GET` | `/api/stats` | Get live dashboard analytics counts |

---

## ⚙️ Local Setup Instructions

### Prerequisites
- Python 3.12+
- pip
- Git

### Step 1 — Clone the Repository
```bash
git clone https://github.com/MalayJoshi1/customer-support-ticket-crm-datastraw.git
cd customer-support-ticket-crm-datastraw
```

### Step 2 — Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run the Server
```bash
uvicorn main:app --reload
```

### Step 5 — Open in Browser
```
http://127.0.0.1:8000
```

> The frontend is served directly by FastAPI — no separate frontend server or build step needed.

---

## 🚢 Deployment on Railway

### Step 1 — Connect GitHub on Railway
1. Go to [railway.app](https://railway.app) and sign in with GitHub
2. Click **New Project → Deploy from GitHub repo**
3. Select `customer-support-ticket-crm-datastraw`
4. Go to **Settings → Networking → Generate Domain**
5. Railway auto-detects Python and deploys using the `Procfile`

---

## 🧠 Architecture Decisions

- **FastAPI over Flask** — automatic API docs at `/docs`, built-in type validation, modern async support
- **SQLAlchemy ORM** — clean model definitions, relationship management, cascade deletes, no raw SQL
- **Pydantic schemas** — strict input validation with EmailStr, separate request and response models
- **Vanilla JS** — zero framework overhead, no build step, works directly with FastAPI static files
- **Single HTML file frontend** — easy to serve, no npm, no bundler, instant deployment
- **Soft status system** — tickets are never deleted, only Closed — preserves full audit history
- **Debounced search** — 300ms debounce prevents excessive API calls while typing

---

<p align="center">Built with ❤️ by Malay Joshi</p>
