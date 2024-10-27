# cscript/runner.py
import sys
import os
import subprocess
import pkg_resources
from .core.generator import MachineCodeGenerator
from .core.parser import Parser

def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: cscript <filename.cript> or cscript update")
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

            # Parsa och kör koden
            parser = Parser()
            generator = MachineCodeGenerator()

            try:
                tokens = parser.parse_code(content)
                machine_code = generator.generate_machine_code(tokens)
                generator.execute_code(machine_code)  # Detta ska nu bara visa resultatet

            except RuntimeError as e:
                error_msg = str(e)
                if "SYNTAX ERROR" in error_msg:
                    print("\033[91m" + error_msg + "\033[0m")
                    print(f"Check your CScript syntax in {filename}")
                else:
                    print("\033[93m" + "Internal compiler error:" + "\033[0m")
                    print(error_msg)
                sys.exit(1)

        except Exception as e:
            print(f"\033[91mError: {str(e)}\033[0m")
            sys.exit(1)

    except Exception as e:
        print(f"\033[91mUnexpected error: {str(e)}\033[0m")
        sys.exit(1)