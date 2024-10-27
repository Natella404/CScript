# cscript/runner.py
import sys  # Lade till denna import
import os
import subprocess
import pkg_resources
from .core.generator import MachineCodeGenerator
from .core.parser import Parser
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
                print(f"\033[94mProcessing file: {filename}\033[0m")  # Blå text
                print(f"\033[93mFile contents:\033[0m")  # Gul text
                print(content)
                print("\033[94m-------------------\033[0m")  # Blå linje

            # Parsa och generera kod
            parser = Parser()
            generator = MachineCodeGenerator()

            try:
                # Försök parsa koden
                tokens = parser.parse_code(content)
                print("\033[93mTokens generated:\033[0m", tokens)  # Visa tokens

                # Generera maskinkod
                machine_code = generator.generate_machine_code(tokens)
                print("\033[93mMachine code generated:\033[0m", machine_code)  # Visa maskinkod

                # Kör koden
                if generator.execute_code(machine_code):
                    print("\033[92mProgram executed successfully!\033[0m")
                else:
                    print("\033[91mExecution failed.\033[0m")

            except RuntimeError as e:
                error_msg = str(e)
                if "SYNTAX ERROR" in error_msg:
                    print("\033[91m" + error_msg + "\033[0m")
                    print(f"Check your CScript syntax in {filename}")
                else:
                    print("\033[93m" + "Internal compiler error:" + "\033[0m")
                    print(error_msg)
                    print("Please report this bug!")
                sys.exit(1)

        except Exception as e:
            print(f"\033[91mError: {str(e)}\033[0m")
            sys.exit(1)

    except Exception as e:
        print(f"\033[91mUnexpected error: {str(e)}\033[0m")
        sys.exit(1)