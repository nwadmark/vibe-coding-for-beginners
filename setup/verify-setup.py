"""Verify your environment is ready for the Vibe Coding workshop."""

import sys

def check_python_version():
    v = sys.version_info
    if v.major >= 3 and v.minor >= 8:
        print(f"  ✅ Python {v.major}.{v.minor}.{v.micro}")
        return True
    else:
        print(f"  ❌ Python {v.major}.{v.minor}.{v.micro} — version 3.8 or higher is required")
        print("     Fix: Download Python 3.10+ from https://python.org/downloads")
        return False

def check_stdlib():
    libs = ["math", "json", "datetime", "random", "csv", "os"]
    all_ok = True
    for lib in libs:
        try:
            __import__(lib)
            print(f"  ✅ {lib}")
        except ImportError:
            print(f"  ❌ {lib} — this is a built-in library and should not be missing")
            print(f"     Fix: Reinstall Python from https://python.org/downloads")
            all_ok = False
    return all_ok

def check_optional():
    try:
        __import__("streamlit")
        print("  ✅ streamlit (installed)")
    except ImportError:
        print("  ℹ️  streamlit (not installed — optional, needed for dashboard projects)")
        print("     Install later with: pip install streamlit")

def main():
    print()
    print("🔍 Vibe Coding for Beginners — Setup Check")
    print("=" * 45)

    print("\n📌 Python Version")
    python_ok = check_python_version()

    print("\n📌 Standard Libraries")
    stdlib_ok = check_stdlib()

    print("\n📌 Optional Libraries")
    check_optional()

    print("\n" + "=" * 45)
    if python_ok and stdlib_ok:
        print("🎉 You are ready to go! Head to build/01-decision-framework/ to start.")
    else:
        print("⚠️  Your setup needs attention. Fix the issues marked with ❌ above.")
    print()

if __name__ == "__main__":
    main()
