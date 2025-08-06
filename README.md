# 📁 Generate Project Structure

This Python script helps you automatically generate a beautiful, Markdown-friendly project folder structure. It's perfect for documenting your project's layout in `README.md` files — with icons for folders 📁 and files 📄, and support for excluding specific items.

---

## 🚀 Features

- Recursively scans any folder structure
- Outputs a clean, readable tree format
- Uses 📁 for folders and 📄 for files
- Allows skipping specified folders and files (e.g., `__pycache__`, `.git`, `node_modules`, etc.)
- Ideal for use in project documentation

---

## 🧰 Requirements

- Python 3.6 or higher
- Works on Windows, macOS, and Linux

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/ssr-1998/Generate-Project-Structure.git
cd Generate-Project-Structure
```

---

## ⚙️ Usage

Run the script inside the root of your project folder:

```bash
python main.py
```

This will output the project structure in your terminal window.

If you want to save the output to a file (e.g., to paste into your README.md), use:

```bash
python main.py > structure.txt
```

❓ What's the difference?
- `python main.py`: Displays the project structure directly in the terminal window.

- `python main.py > structure.txt`: Redirects the output to a file named structure.txt, which is useful for copy-pasting into your documentation or saving for later.

---

## 🧾 Sample Output

```text
📁 my_project
├── 📁 src
│   ├── 📄 main.py
│   └── 📄 utils.py
├── 📁 tests
│   └── 📄 test_main.py
└── 📄 README.md
```

---

## ✏️ Configuration

You can change the following variables inside project_structure.py:

```python
ROOT_DIR = os.path.abspath(".")  # Change this to target a different Directory

EXCLUDE = {"__pycache__", ".git", ".vscode", "venv"}  # Add/Remove excluded Folders or Files
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
