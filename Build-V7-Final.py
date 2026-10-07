import sys, os, shutil, subprocess, pathlib

print("="*70)
print("SJ Group - V7 GENERIC EXE Builder (Python Script)")
print("Main File: PDF-Ledger-Reconciler-V7-Generic-Any-Invoice-Series.py")
print("="*70)

# Exact file name with hyphens
PY_FILE = "PDF-Ledger-Reconciler-V7-Generic-Any-Invoice-Series.py"
EXE_NAME = "SJGroup_Reconciler_V7_Generic"

# Check file exists, also check for double extension
if not os.path.exists(PY_FILE):
    # Check double .py.py
    if os.path.exists(PY_FILE + ".py"):
        print(f"[FIX] Renaming {PY_FILE}.py -> {PY_FILE}")
        os.rename(PY_FILE + ".py", PY_FILE)
    else:
        print(f"[ERROR] File not found: {PY_FILE}")
        print("\nFolder me ye .py files hain:")
        for f in pathlib.Path(".").glob("*.py"):
            print(f"  - {f}")
        input("Press Enter...")
        sys.exit(1)

print(f"[OK] Found: {PY_FILE}")

print("\n[1/3] Installing libraries...")
os.system("pip install --upgrade pip")
os.system("pip install PyMuPDF openpyxl pyinstaller")

print("\n[2/3] Cleaning old builds...")
for d in ["build", "dist", "__pycache__"]:
    if os.path.exists(d):
        shutil.rmtree(d, ignore_errors=True)
        print(f"Deleted {d}")
for f in pathlib.Path(".").glob("*.spec"):
    if "SJGroup" in str(f):
        os.remove(f)
        print(f"Deleted {f}")

print(f"\n[3/3] Building EXE from {PY_FILE}...")
print("This will take 3-5 minutes, do NOT close...")

cmd = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",
    "--windowed",
    "--name", EXE_NAME,
    "--hidden-import=fitz",
    "--hidden-import=openpyxl",
    "--hidden-import=openpyxl.styles",
    "--clean",
    PY_FILE
]

print(f"\nCommand: {' '.join(cmd)}\n")
result = subprocess.run(cmd)

exe_path = os.path.join("dist", f"{EXE_NAME}.exe")
if os.path.exists(exe_path):
    size_mb = os.path.getsize(exe_path) / (1024*1024)
    print("\n" + "="*70)
    print(f"SUCCESS! EXE BAN GAYA!")
    print(f"Location: {os.path.abspath(exe_path)}")
    print(f"Size: {size_mb:.1f} MB")
    print("="*70)
    print("\nFeatures:")
    print("- Kisi bhi PC par bina Python ke chalega")
    print("- ANY Invoice Series: DS/, RS/, SMI/CG, INV-, BILL/, TDS-, GST/")
    print("- 500+ Creditors ke liye generic")
    print("- 4 Themes + Color Coded Results")
else:
    print("\n" + "="*70)
    print("FAILED! EXE nahi bana")
    print("Solutions:")
    print("1. CMD ko Run as Administrator se chalao")
    print("2. Antivirus 5 min band karo")
    print("3. Folder C:\\SJGroup me rakho (space bina path)")
    print("4. Python 3.11 ya 3.12 use karo")
    print("="*70)

input("\nPress Enter to exit...")
