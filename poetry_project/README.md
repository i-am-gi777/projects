# Poetry Project: Step-by-Step Setup (poetry_project)

This document explains everything done in the poetry_project folder using **Poetry** for Python dependency management.

---

# 1. Project Creation

The project was created using Poetry:

```bash
poetry new poetry_project 
```

This generated the basic structure:

```
poetry_project /
 ├── pyproject.toml
 ├── README.md
 ├── src/
 └── tests/
```

---

# 2. Understanding pyproject.toml

The file `pyproject.toml` is the **main configuration file** for Poetry.

It contains:

- Project metadata (name, version)
- Python version requirement
- Dependencies
- Tool configurations

Example:

```toml
[tool.poetry]
name = "poetry_project "
version = "0.1.0"

[tool.poetry.dependencies]
python = ">=3.11,<3.14"
```

---

# 3. Adding Dependencies

Packages were added using Poetry:

```bash
poetry add pandas
```

This installs:

- pandas library
- creates virtual environment
- updates pyproject.toml
- generates poetry.lock file

Later missing dependency was fixed:

```bash
poetry add openpyxl
```

(Required for Excel file writing)

---

#  4. Virtual Environment Handling

Poetry automatically created and managed virtual environments:

- First detected Python version mismatch
- Switched from Python 3.8 → Python 3.13
- Created a new virtual environment

Example output:

```
Creating virtualenv poetry_project -py3.13
```

---

# 5. Running the Script

The Python script was executed using Poetry:

```bash
poetry run python csv_to_excel.py
```

This ensures:

- correct Python version is used
- dependencies are loaded from Poetry environment

# 7. Final Working Flow

The final working workflow is:

```bash
poetry install
poetry add pandas
poetry add openpyxl
poetry run python csv_to_excel.py
```

---

# 8. Summary

In this project, we learned:

- How to create a Poetry project
- How Poetry manages virtual environments
- How to add dependencies
- How to run Python scripts with Poetry
- How to fix common errors
- How Poetry handles Python version conflicts

---

# Key Takeaway

Poetry ensures:

- isolated environments per project
- reproducible dependencies
- clean project management

---

# Project Status

✔ Setup completed ✔ Dependencies installed ✔ Script executed successfully after fixes

