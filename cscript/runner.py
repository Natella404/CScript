# cscript/runner.py
import sys
import os
import subprocess
import pkg_resources
from .core.generator import MachineCodeGenerator
from .core.parser import Parser

def show_welcome():
    version = pkg_resources.get_distribution('cscript').version
    print(f"""
    CScript v{version}
    Type 'cscript help' for commands
    """)

def update_cscript():
    try:
        print("\033[92mChecking for updates...\033[0m")  # Grön text
        subprocess.check_call([
            sys.executable, 
            '-m', 
            'pip', 
            'install', 
            '--upgrade',
            'git+https://github.com/Natella404/CScript.git'
        ])
        print("\033[92mCScript has been updated successfully!\033[0m")
    except subprocess.CalledProcessError as e:
        print("\033[91mError updating CScript:\033[0m", str(e))  # Röd text
        return False
    return True

def show_help():
    print("""
    CScript Commands:
    ----------------
    cscript <filename.cript>  - Run a CScript file
    cscript update           - Update CScript to latest version
    cscript help             - Show this help message

    Example:
    cscript myscript.cript
    """)

def main():
    try:
        if len(sys.argv) < 2:
            show_welcome()
            show_help()
            return

        command = sys.argv[1].lower()

        # Hantera kommandon
        if command == "help":
            show_help()
            return
        elif command == "update":
            update_cscript()
            return

        # Kör CScript-fil
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print(f"\033[91mError: File '{filename}' not found\033[0m")
            return

        try:
            # Läs filen
            with open(filename, 'r') as file:
                content = file.read()

            # Parsa och generera kod
            parser = Parser()
            generator = MachineCodeGenerator()

            try:
                # Försök parsa koden
                tokens = parser.parse_code(content)

                # Generera maskinkod
                machine_code = generator.generate_machine_code(tokens)

                # Kör koden
                if generator.execute_code(machine_code):
                    print("\033[92mProgram executed successfully!\033[0m")
                else:
                    print("\033[91mExecution failed.\033[0m")

            except RuntimeError as e:
                error_msg = str(e)
                if "SYNTAX ERROR" in error_msg:
                    print("\033[91m" + error_msg + "\033[0m")  # Röd text för syntaxfel
                    print(f"Check your CScript syntax in {filename}")
                else:
                    print("\033[93m" + "Internal compiler error:" + "\033[0m")  # Gul text
                    print(error_msg)
                    print("Please report this bug!")
                sys.exit(1)

        except Exception as e:
            print(f"\033[91mError: {str(e)}\033[0m")
            sys.exit(1)

    except Exception as e:
        print(f"\033[91mUnexpected error: {str(e)}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()