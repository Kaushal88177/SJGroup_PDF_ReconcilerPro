# SJ Group - PDF Ledger Reconciler Pro

### 100% Generic Edition - Any Invoice Series Support

A powerful, offline desktop tool to reconcile Tally/Accounting  PDF ledgers with party statements. Built for Indian businesses handling 500+ Transactions per creditors with different invoice series.

[Python](https://img.shields.io/badge/Python-3.11%2B-blue)
[License](https://img.shields.io/badge/License-MIT-green)
[Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)
[Status](https://img.shields.io/badge/Status-Production%20Ready-success)

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

## 📦 Installation

### Option 1: Use EXE (No Python Needed) - Recommended for Users

1. Download `SJGroup_Reconciler_V7_Generic.exe` from Releases
2. Double-click to run on any Windows PC (No Python required)
3. Select Party PDF and Our Tally PDF → Reconcile

### Option 2: Run from Source (For Developers)

```bash
# Clone repo
git clone https://github.com/yourusername/PDF-Ledger-Reconciler-V7-Generic.git
cd PDF-Ledger-Reconciler-V7-Generic

# Install dependencies
pip install -r requirements.txt

# Run
python PDF-Ledger-Reconciler-V7-Generic-Any-Invoice-Series.py
```

**Requirements:**
```
PyMuPDF==1.24.9
openpyxl==3.1.2
```

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
4. **Click "GENERIC RECONCILE V7"**
5. **Check Results:**
   - Summary cards on top
   - Colored list + Detailed table
   - Excel auto-saved on Desktop

---

## 🧪 Tested Cases

### Highway Tyres Example
- **Party:** Highway_Tyres.pdf (26 entries)
- **Our:** Starex-Highway.pdf (26 entries)
- **Result:** 24/26 Matched (92%)
  - 7 Invoices: `DS/24-25/0130`, `DS/24-25/0244`, etc → All Matched
  - Bank: HDFC vs ICICI name diff ignored

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

## 🤝 Contributing

1. Fork the repo
2. Create feature branch: `git checkout -b feature`
3. Commit: `git commit -m 'Add feature'`
4. Push: `git push origin feature`
5. Open Pull Request

---

## 📝 Changelog

### V7.0 GENERIC (Latest) - Oct 2024
- ✅ 100% Generic invoice extractor (any series)
- ✅ Supports 500+ creditors
- ✅ Min amount logic for 2-amount lines
- ✅ Party Debit=Our Credit logic

### V6.0 Highway Tyres Fixed
- ✅ Fixed DS/24-25/ pattern
- ✅ Highway Tyres tested (92% match)

### V5.0 Smart Party Logic
- ✅ Party Receipt = Our Payment logic
- ✅ Date tolerance + Ignore Date option

### V4.0 Full Color
- ✅ 4 Themes + Color Coded

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

---

## 🔗 Links

- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [openpyxl](https://openpyxl.readthedocs.io/)
- [PyInstaller](https://pyinstaller.org/)

---

**Made with ❤️ for Indian Accountants & Businesses**
