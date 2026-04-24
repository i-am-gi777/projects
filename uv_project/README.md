#  UV Project: Step-by-Step Setup (uv_project)

This document explains everything done in the `uv_project` folder using **uv** for Python dependency and environment management.

---

# 1. Project Creation

The project was initialized using uv:

```bash
uv init uv_project
```

This created a basic project structure:

```
uv_project/
 ├── pyproject.toml
 ├── main.py (or script files added manually)
 └── .venv/ (created automatically later)
```

---

# 2. Understanding pyproject.toml

The file `pyproject.toml` is the **main project configuration file**.

It contains:

- Project metadata (name, version)
- Python version requirement
- Dependencies

Example:

```toml
[project]
name = "uv_project"
version = "0.1.0"
dependencies = []

requires-python = ">=3.11,<3.14"
```

---

# 3. Adding Dependencies

Packages were added using uv:

```bash
uv add pandas
```

This automatically:

- Creates a virtual environment (.venv)
- Installs pandas
- Updates pyproject.toml
- Creates/updates lock information

Later missing dependency was fixed:

```bash
uv add openpyxl
```

(Required for Excel file writing support)

---

# 4. Virtual Environment Handling

uv automatically manages virtual environments inside the project.

During execution:

- It detected Python version mismatch initially
- Switched to a compatible Python version (3.13)
- Created `.venv` inside project directory

Example behavior:

```
Using python3.13 (3.13.x)
Creating virtual environment .venv
```

---

# 5. Running the Script

The Python script was executed using uv:

```bash
uv run python csv_to_excel.py
```

This ensures:

- correct Python version is used
- dependencies are loaded from `.venv`
- project environment is isolated



# 7. Final Working Flow

The final working workflow using uv is:

```bash
uv init my_project
cd my_project
uv add pandas
uv add openpyxl
uv run python csv_to_excel.py
```

---

# 8. Summary

In this project, we learned:

- How to create a uv project
- How uv manages virtual environments automatically
- How to add dependencies quickly
- How to run Python scripts using uv
- How to fix missing dependency errors
- How uv handles Python version selection

---

# Key Takeaway

uv provides:

- extremely fast dependency installation
- automatic virtual environment management
- simple and clean workflow
- modern replacement for pip + venv in many cases

---

# Project Status

✔ Project initialized ✔ Dependencies installed ✔ Script executed successfully after fixes

