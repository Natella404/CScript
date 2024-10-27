# ide_setup.py
import os
import sys
import subprocess

def setup_file_association():
    """Registrerar .cript filändelsen"""
    if os.name == 'nt':  # Windows
        # Windows-specifik registrering
        subprocess.run(['assoc', '.cript=CScriptFile'])
        subprocess.run(['ftype', 'CScriptFile=cscript.exe %1 %*'])
    else:  # Linux/Mac
        # Unix-baserad registrering
        home = os.path.expanduser("~")
        with open(f"{home}/.bashrc", "a") as bashrc:
            bashrc.write("\nalias cscript='python -m cscript.runner'")

def main():
    try:
        setup_file_association()
        print("CScript har installerats framgångsrikt!")
        print("Du kan nu köra .cript filer med kommandot: cscript filnamn.cript")
    except Exception as e:
        print(f"Ett fel uppstod vid installation: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()