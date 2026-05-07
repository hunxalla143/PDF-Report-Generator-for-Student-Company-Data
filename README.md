# PDF-Report-Generator-for-Student-Company-Data

## Project Overview

PDF Report Generator is a Python-based application designed to generate professional PDF reports for student and company data. The system supports CSV/JSON data loading, manual data entry, chart generation, password-protected PDFs, and automatic report storage.

This project simulates real-world reporting systems used in schools, universities, and companies.

---

# Features

## Student Report
- Student details
- Course information
- Marks
- Attendance
- Performance chart

## Company Report
- Employee details
- Role information
- Performance summary

## Data Input Methods
- Manual data entry
- CSV file loading
- JSON file loading

## PDF Features
- Professional formatting
- Tables
- Headings
- Date & time
- Logo support
- Charts/graphs
- Automatic file saving

## Security
- Password-protected PDFs

## Error Handling
- Missing files
- Invalid data
- Invalid images
- Empty data handling

## Modular Structure
- Separate modules for:
  - PDF generation
  - Data loading
  - Charts
  - Security
  - Utilities

---

# Technologies Used

- Python 3.13
- ReportLab
- Matplotlib
- PyPDF2

---

# Project Structure

```text
PDF Report Generator/
│
├── main.py
├── pdf_generator.py
├── data_loader.py
├── charts.py
├── security.py
├── utils.py
│
├── assets/
│   ├── logo.png
│   └── chart.png
│
├── reports/
│
├── data/
│   ├── students.csv
│   ├── employees.csv
│   └── students.json
│
└── README.md
