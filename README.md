# Folder Sorter

A simple command-line tool that organizes files into subfolders based on their file extensions.

The project started as a JavaScript/Node.js script and now also includes a Python implementation. The Python version uses only the Python standard library, so no third-party packages are required.

## Features

- Sorts files into folders named after their extensions (e.g. `PDF`, `PNG`, or `TXT`).
- Places files without an extension in `Ohne_Endung`.
- Uses the user's Downloads folder by default.
- Allows you to specify a custom folder.
- Includes a dry-run mode to preview changes without moving files.
- Prevents overwriting existing files by adding a numeric suffix to duplicate filenames.
- Processes files in the selected folder only (no recursive subfolder scanning).

## Requirements

- Python 3.7 or newer
- No external Python packages required

## Usage

Open a terminal in the directory containing `folder_sorter.py`.

### Sort the Downloads folder

If no folder is specified, the script automatically uses the current user's Downloads folder.

```bash
python folder_sorter.py
```

### Sort a specific folder

Pass the folder path as the first argument.

**Windows:**

```powershell
python folder_sorter.py "C:/Users/YourName/Downloads"
```

**Linux / macOS:**

```bash
python3 folder_sorter.py "/home/yourname/Downloads"
```

### Preview changes (Dry Run)

Use `--dry-run` to display the planned file movements without actually moving any files.

```bash
python folder_sorter.py --dry-run
```

Or specify a custom folder:

```bash
python folder_sorter.py "D:/Files" --dry-run
```

### Show help

```bash
python folder_sorter.py --help
```

## Example

**Before:**

```text
Downloads/
├── invoice.pdf
├── photo.png
├── notes.txt
├── archive
└── README
```

**After:**

```text
Downloads/
├── PDF/
│   └── invoice.pdf
├── PNG/
│   └── photo.png
├── TXT/
│   └── notes.txt
├── Ohne_Endung/
│   ├── archive
│   └── README
```

Folder names are based on the file extension and converted to uppercase. Files without an extension are placed in `Ohne_Endung`.

If a file with the same name already exists in the destination folder, a number is added to the filename.

For example:

```text
invoice.pdf
invoice_1.pdf
invoice_2.pdf
invoice_3.pdf
```

## How it works

1. Reads the files directly inside the selected folder.
2. Determines the file extension.
3. Creates the corresponding destination folder if necessary.
4. Checks whether the destination filename already exists.
5. Moves the file to its destination (unless dry-run mode is enabled).

Existing subfolders are not processed, and their contents remain unchanged.

## Project files

- `folder_sorter.py` – Python implementation (recommended)
- `sorter.js` – Original JavaScript implementation
