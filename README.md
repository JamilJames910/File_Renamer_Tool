# File Renamer CLI 🗂️

A simple, intuitive, and safe Python command-line tool to **rename all files in a folder with custom numbering and prefixes**. Perfect for organizing photos, documents, or any batch of files.

---

## Features ✨

- ✅ Rename all files in a specified folder in **alphabetical order**.
- ✅ Keep original file extensions intact.
- ✅ Customize file prefixes and starting numbers.
- ✅ Handles invalid paths gracefully with helpful feedback.
- ✅ Works across different operating systems (Windows, macOS, Linux).

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Installation 🛠️

1. Clone this repository:

```bash
git clone https://github.com/your-username/File_Renamer_CLI.git
cd File_Renamer_CLI
````

2. Make sure you have **Python 3.x** installed.

3. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

4. No additional dependencies are required—Python's built-in `os` module handles everything.

---

## Usage 💻

Run the script:

```bash
python rename_files.py
```

You will be prompted to:

1. **Enter the folder path** containing files.
2. **Enter a prefix** for renamed files (default is `file`).
3. **Enter a starting number** (default is `1`).

The tool will rename all files in the folder and provide a log of renamed files.

---

### Example

```
Enter folder path: /Users/username/Desktop/photos
Enter file prefix (default 'file'): vacation
Enter starting number (default 1): 10
```

**Output:**

```
✅ Found folder: '/Users/username/Desktop/photos'
Renamed: IMG001.jpg -> vacation_10.jpg
Renamed: IMG002.jpg -> vacation_11.jpg
...
✅ All files have been renamed.
```

---

## Project Structure 🗂️

```
File_Renamer_CLI/
├── rename_files.py        # Main script
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

---

## Contributing 🤝

Contributions, suggestions, and improvements are welcome!

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.


---

## Contact ✉️

Created with ❤️ by \ Jamil James
GitHub: https://github.com/JamilJames910
Email:  Jamil.i.James1@gmail.com
