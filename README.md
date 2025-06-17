
# 🧾 Inventory Management System (Python CLI App)

A lightweight Python-based command-line inventory system that allows users to manage product stock by name or barcode. Includes features to add new items, restock, sell items, and view inventory — all with data saved to a JSON file for persistence.

---

## ✅ Features
- Add new items with name, barcode, price, and quantity
- Search and update stock by name or barcode
- Restock and reduce inventory
- View remaining stock levels
- Data is saved and loaded automatically from `stock.json`
- Simple and interactive command-line interface

---

## 🛠 Technologies Used
- Python 3
- JSON for file-based storage
- Built-in modules: `os`, `json`

---

## 🚀 How to Run
```bash
python inventory.py
```

---

## 🧠 Concepts Practiced
- Input validation using `try`/`except`
- Working with lists and dictionaries
- File handling (read/write JSON)
- Menu-based navigation using loops
- Real-world application logic

---

## 📦 File Overview
| File        | Description                           |
|-------------|----------------------------------------|
| `inventory.py` | Main Python script                  |
| `stock.json`   | Auto-created data file to store inventory |

---

## 🔮 Future Improvements
- Add search by partial name
- Display item prices in inventory report
- Export inventory to CSV
- Add transaction logs
- GUI version using Tkinter or Flask

---

## 🪪 License
MIT License — Free to use, modify, and distribute.
