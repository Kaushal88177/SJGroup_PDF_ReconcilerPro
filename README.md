# SJ Group - PDF Ledger Reconciler Pro

### 100% Generic Edition - Any Invoice Series Support
*** ScreenShot : https://github.com/Kaushal88177/SJGroup_PDF_ReconcilerPro/tree/f7de4e71784d5dce55e2007d2e5aaf85947f57ca/ScreenShot ***

A powerful, offline desktop tool to reconcile Tally/Accounting  PDF ledgers with party statements. Built for Indian businesses handling 500+ Transactions per creditors with different invoice series.

> Built by **Kaushal Verma** | Real-world accounting automation | 90% time saved

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20EXE-green?style=for-the-badge&logo=windows)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---
## 🚀 Features

### Generic Invoice Support
- **No Hardcoded Series** - Works with ANY invoice format:
  - `DS/24-25/0130`, `RS/24-25/2131`
  - `SMI/CG26-27/0258`, `SMI/CG/24-25/001`
  - `INV-001`, `INV/2024/123`, `BILL/2024/001`
  - `TDS-1092`, `GST/24-25/001`, `2024/INV/001`
  - Any alphanumeric with `/` or `-`
- **500+ Creditors Ready** - One software for all parties

### Smart Accounting Logic
- **Party Debit = Our Credit** | **Party Credit = Our Debit**
- **Party Receipt = Our Payment** | **Party Payment = Our Receipt**
- Bill No + Amount based matching (Primary)
- Date Tolerance (0-60 days configurable)
- Ignore Date Completely option
- Cheque No vs Receipt No difference ignored (Bank entries)
- To/By and Dr/Cr opposite logic handled

### Smart Amount Extraction
- Handles PDFs where one line has 2 amounts (Transaction + Balance)
- Example: `DS/24-25/0130 25,100.00 25,34,296.60 Dr` → Correctly picks `25,100.00`

### Beautiful UI
- 4 Professional Themes:
  - Light Professional
  - Dark Modern
  - SJ Group Blue
  - Emerald Accounting
- Color Coded Results:
  - 🟢 Green = Match
  - 🔴 Red = Only in Party
  - 🟠 Orange = Only in Our Books
  - 🔵 Blue = Bank Only
- Summary Cards + Detailed Tables

### Excel Export
- Color-coded Excel with 4 sheets:
  1. Summary (Opening/Closing diff)
  2. Party Detailed
  3. Our Books Detailed
  4. Differences Only (Action Items)
- Auto-saves to Desktop/SJGroup_PDF_Output

---
## 📖 How to Use

1. **Open Software** (EXE or Python)
2. **Select PDFs:**
   - 1st: Party Statement PDF (e.g., Highway_Tyres.pdf)
   - 2nd: Our Tally Ledger PDF (e.g., Starex-Highway.pdf)
3. **Set Tolerance:**
   - Amt Tolerance: Rs 2.00 (default)
   - Date Tolerance: 10 days (default)
   - Tick "Ignore Date" if dates differ a lot
4. **Click ["GENERIC RECONCILE V7"](https://github.com/Kaushal88177/SJGroup_PDF_ReconcilerPro/releases/download/v7.0-generic/SJGroup_Reconciler_V7_Generic.exe)**
5. **Check Results:**
   - Summary cards on top
   - Colored list + Detailed table
   - Excel auto-saved on Desktop

---
## 📁 Project Structure

```
.
├── PDF-Ledger-Reconciler-V7-Generic-Any-Invoice-Series.py  # Main App
├── Build_V7_FINAL_EXE.bat                                   # EXE Builder (BAT)
├── build_v7_final.py                                        # EXE Builder (Python)
├── SJGroup_V7_Generic.spec                                  # PyInstaller Spec
├── requirements.txt                                         # Dependencies
├── README.md                                                # This file
└── dist/
    └── SJGroup_Reconciler_V7_Generic.exe                   # Final EXE (after build)
```

---

## 🔧 Technical Details

### Generic Invoice Extractor (V7 Core)
```python
def extract_invoice_generic(line):
    # Any token with / or - and alphanumeric
    # Length >=4, contains digit, not a date
    # Examples: DS/24-25/0130, INV-123, BILL/2024/001
    pattern = r"\b([A-Z0-9]{1,}(?:[/-][A-Z0-9]+){1,})\b"
    # Filters out dates like 10-Apr-24
```

### Amount Extraction Fix
```python
# Line has 2 amounts: txn + balance
# Example: "DS/24-25/0130 25,100.00 25,34,296.60 Dr"
amounts = [25,100.00, 25,34,296.60]
amount = min(amounts)  # Picks transaction amount
```

---
## 📄 License

MIT License - Free for commercial use

---

## 👨‍💻 Author

**Kunal Verma - SJ Group**
- Location: Bhilai, Chhattisgarh, India
- Use Case: Reconciling 500+ creditor ledgers from Tally PDFs

---

## ⭐ Star & Support

If this tool saves your time in ledger reconciliation, please star the repo!

**For Issues:** Open GitHub Issue with PDF sample (remove sensitive data) and screenshot.

**Made with ❤️ for Indian Accountants & Businesses**
