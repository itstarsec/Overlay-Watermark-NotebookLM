# PDF Logo Stamper

A lightweight Python tool that stamps a PNG logo or watermark image onto every page of a PDF document using PyMuPDF.

This tool is useful for adding company logos, confidentiality marks, approval stamps, report branding, or custom visual overlays to exported PDF reports.

---

## What It Does

### PNG Overlay on PDF

This tool inserts a PNG image into a fixed position on every page of a PDF file.

It is designed for use cases such as:

- Adding a company logo to PDF reports
- Adding a confidentiality stamp
- Adding a visual mark to presentation exports
- Branding security assessment reports
- Replacing manual PDF editing with automation

The current implementation uses PyMuPDF to directly modify PDF pages without converting the whole PDF into images. This helps preserve the original PDF quality, text, and layout.

---

## Features

- Add a PNG image to every page of a PDF
- Preserve the original PDF structure and quality
- Support transparent PNG logos
- Configurable output filename
- Simple Python script, easy to customize
- Works on Windows, Linux, and macOS
- Suitable for report branding and document automation

---

## Supported Formats

### Input

- PDF documents: `.pdf`
- PNG image: `.png`

### Output

- Stamped PDF document: `.pdf`

---

## Use Cases

Example:

```text
Cybersecurity_Blueprint.pdf
```

can be stamped with:

```text
your_logo.png
```

and exported as:

```text
Cybersecurity_Blueprint.stamped.pdf
```

---

## Legal Disclaimer

This tool is intended for legitimate document editing and branding purposes only.

You should only use this tool on PDF files that you own, created yourself, or have permission to modify.

The author does not encourage or support the removal, replacement, or modification of third-party copyright notices, ownership marks, attribution marks, or protected watermarks without proper authorization.

---

## Getting Started

### 1. Clone or Download the Project

```bash
git clone https://github.com/itstarsec/Overlay-Watermark-NotebookLM.git
cd Overlay-Watermark-NotebookLM
```

Or simply place the script in a working folder:

```text
overlay.py
Cybersecurity_Blueprint.pdf
your_logo.png
```

---

## 2. Create a Python Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

Install PyMuPDF:

```bash
pip install pymupdf
```
---

## How to Use

Run the script:

```bash
python overlay.py
```

By default, the script will use the following files:

```python
input_pdf="Cybersecurity_Blueprint.pdf"
png_path="your_logo.png"
output_pdf="Cybersecurity_Blueprint.stamped.pdf"
```

Make sure these files exist in the same directory as `overlay.py`.

---

## Project Structure

```text
pdf-logo-stamper/
├── overlay.py
├── README.md
├── your_logo.png
└── Cybersecurity_Blueprint.pdf
```

---

## Requirements

- Python 3.8+
- PyMuPDF

Install dependency:

```bash
pip install pymupdf
```

---

## Roadmap

Planned improvements:

- Command-line arguments support
- Batch processing for multiple PDF files
- Support for custom logo position
- Support for opacity control
- Support for page range selection
- Preview mode for first page
- Windows EXE build with PyInstaller

---

## Contributing

Pull requests are welcome.

You can contribute by improving:

- CLI support
- Batch processing
- Dynamic positioning
- Error handling
- Documentation
- Windows executable build script

---

## License

MIT License

You are free to use, modify, and distribute this project under the terms of the MIT License.
