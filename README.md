# python-projects
Python Projects by  Zulqarnain Khan Jadoon
# Enterprise IT Support Ticket & Inventory Management System

A robust, production-ready Command-Line Interface (CLI) application built with **Python 3** and **SQLite3**. This system efficiently models and tracks IT support tickets, hardware/software assets, and user assignments using a highly normalized relational database architecture.

Designed specifically to demonstrate solid backend engineering principles, database integrity, and scalable modular code structure for IT service management (ITSM) workflows.

---

## 🚀 Key Features

* **Relational Database Engine:** Built on SQLite3 with proper primary/foreign key constraints, cascading deletes, and indexes for optimized query performance.
* **Ticket Lifecycle Management:** Complete tracking of support tickets from initialization (`Open`), through investigation (`In Progress`), to resolution (`Resolved`/`Closed`).
* **Inventory & Asset Tracking:** Maps hardware and software assets to specific technical departments and monitors device health status.
* **Operational Metrics & Reporting:** Built-in analytical queries to pull key performance metrics, such as open ticket counts, average resolution bottlenecks, and asset-to-user ratios.
* **Robust Data Validation:** Strict inputs handling, secure state transitions, and error handling to prevent database corruption or SQL injection vulnerabilities.

---

## 📊 Database Schema Layout

The system utilizes a 3NF (Third Normal Form) relational structure to eliminate redundancy and maintain structural integrity:

* **`users`**: Stores staff data, roles, and department locations.
* **`assets`**: Tracks inventory details (Serial Numbers, Device Type, Status).
* **`tickets`**: Manages issue logs, linking a `user_id`, `asset_id`, priority metrics, and timestamp data.

---

## 🛠️ Tech Stack & Concepts Demonstrated

* **Language:** Python 3.x
* **Database:** SQLite3 (Relational Database Management)
* **Architectural Patterns:** Clean separation of concerns (Database Layer vs. Business Logic Layer)
* **Data Serialization:** Structured relational tuples handled safely via Python context managers (`with sqlite3.connect...`)

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/zulqarnainjadoon99/your-repo-name.git](https://github.com/zulqarnainjadoon99/your-repo-name.git)
   cd your-repo-name

---

## 📬 Connect & Collaborate
If you are an international client or recruiter looking for professional AI automation or backend development, feel free to reach out through official channels:

* **LinkedIn:** [Zulqarnain Khan Jadoon on LinkedIn](https://www.linkedin.com/in/zulqarnain-khan-jadoon-4525531a4)
* **Professional Channel:** Verified via OpenTrain AI Specialist Network
