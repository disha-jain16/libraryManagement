# 📚 Library Management System (Python)

A simple **command-line Library Management System** built in Python that allows you to manage books, members, and book loans with support for **exporting and importing data to/from JSON**.

---

## 🧩 Features

* Add, remove, and search books
* Add and remove members
* Borrow and return books
* Track due and overdue books
* Export and import full library data as JSON
* Simple command-line interface

---

## ⚙️ Requirements

* Python 3.7 or higher

No external libraries are required — the system uses only Python's built-in modules (`json`, `uuid`, `datetime`, `dataclasses`).

---

## 🚀 How to Run

```bash
python library_management_system.py
```

---

## 🧠 Usage Guide

When you run the program, you’ll see a simple menu:

```
1. Add book
2. Remove book
3. Search books
4. Add member
5. Borrow book
6. Return book
7. List overdue
8. Export to JSON
9. Import from JSON
10. List books
11. List members
12. List loans
0. Exit
```

### Example Workflow

1. **Add a book** → Enter title, author, year, and number of copies.
2. **Add a member** → Enter name and email.
3. **Borrow a book** → Select a book and member by ID.
4. **Return a book** → Mark a loan as returned.
5. **Export data** → Save all data to a JSON file for backup.

---

## 🧾 JSON Export Example

```json
{
  "books": [
    {
      "id": "f2a4b3...",
      "title": "The Hobbit",
      "author": "J.R.R. Tolkien",
      "year": 1937,
      "copies": 2
    }
  ],
  "members": [
    {
      "id": "7d2c91...",
      "name": "Alice",
      "email": "alice@example.com",
      "joined": "2025-10-05"
    }
  ],
  "loans": []
}
```

---

## 💡 Highlights

* Fully functional CLI interface.
* Data is automatically serialized to JSON for easy sharing or persistence.
* Clean and minimal design — easy to extend for databases or GUIs.

---
