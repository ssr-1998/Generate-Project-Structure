import os

# ✅ Configuration Section

# Set the directory to scan
ROOT_DIR = os.path.abspath(".")

# Skip these folders and files
EXCLUDE = {"__pycache__", ".git", ".vscode", ".DS_Store", ".venv", "node_modules", ".ipynb_checkpoints"}

FOLDER_ICON = "📁"
FILE_ICON = "📄"

def generate_tree(dir_path, prefix=""):
    tree = ""
    items = [item for item in os.listdir(dir_path) if item not in EXCLUDE]
    items.sort()

    for index, item in enumerate(items):
        full_path = os.path.join(dir_path, item)
        connector = "└── " if index == len(items) - 1 else "├── "
        if os.path.isdir(full_path):
            tree += f"{prefix}{connector}{FOLDER_ICON} {item}\n"
            extension = "    " if index == len(items) - 1 else "│   "
            tree += generate_tree(full_path, prefix + extension)
        else:
            tree += f"{prefix}{connector}{FILE_ICON} {item}\n"
    return tree

def main():
    project_name = os.path.basename(ROOT_DIR)
    print(f"{FOLDER_ICON} {project_name}")
    print(generate_tree(ROOT_DIR))
    output = f"{FOLDER_ICON} {project_name}\n" + generate_tree(ROOT_DIR)

    with open("project_structure.txt", "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    main()
