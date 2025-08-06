# 📁 Generate Project Structure

A simple Python script to automatically generate a beautiful, Markdown-friendly project folder structure — complete with folder 📁 and file 📄 icons. It prints the structure to your terminal and also creates a `project_structure.txt` file automatically.

---

## 🚀 Features

- Recursively scans your project directory
- Uses 📁 for folders and 📄 for files
- Automatically excludes common unnecessary files and folders (like `.git`, `__pycache__`, `.ipynb_checkpoints`, etc.)
- Saves output to `project_structure.txt` in UTF-8 format
- Great for documenting your project in a `README.md`

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

## ▶️ Usage

### ✅ Running in the Current Directory

Navigate to your project folder in the terminal and run

```bash
python PATH_TO_generate_project_structure.py
```

For Example:

```bash
python C:\path\to\generate_project_structure\main.py
```

This will:
- Print the folder structure of the current working directory (the folder you're in when you run the command)
- Create `project_structure.txt` in the same folder.

### 🧭 Running from a Different Project Directory

You can use the same script to generate a structure for any project, even if the script itself is stored elsewhere.

- Open terminal inside the target project directory.

- Run:

   ```bash
   python PATH_TO_generate_project_structure.py
   ```

   For Example:

   ```bash
   cd C:\Projects\MyTargetProject
   python C:\Tools\generate-project-structure\main.py
   ```

   This will generate the structure for MyTargetProject.

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

## 🧠 Why We Use `with open(...)` Instead of `> file.txt`

While you could redirect output to a file using:

```bash
python main.py > project_structure.txt
```

This approach causes issues on Windows terminals because they often don't support Unicode (like emoji icons) correctly when using redirection (`>`), leading to garbled output.

Instead, this script uses Python’s built-in `open(..., encoding="utf-8")` to reliably write the output in the correct encoding, so the structure file is clean, portable, and emoji-compatible across platforms and editors.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
