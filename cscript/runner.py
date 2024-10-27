# cscript/runner.py
import sys
import os
import platform
from .core.generator import MachineCodeGenerator

def register_file_extension():
    system = platform.system()

    if system == "Windows":
        import winreg
        # Register .cript extension
        try:
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, ".cript") as key:
                winreg.SetValue(key, "", winreg.REG_SZ, "CScriptFile")

            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "CScriptFile") as key:
                winreg.SetValue(key, "", winreg.REG_SZ, "CScript Source File")
                with winreg.CreateKey(key, "DefaultIcon") as icon_key:
                    # Path to your icon file
                    icon_path = os.path.join(os.path.dirname(__file__), "icons", "cscript.ico")
                    winreg.SetValue(icon_key, "", winreg.REG_SZ, icon_path)
        except Exception as e:
            print(f"Warning: Could not register .cript extension: {e}")

    elif system == "Linux":
        # Create mime type
        mime_path = os.path.expanduser("~/.local/share/mime/packages")
        os.makedirs(mime_path, exist_ok=True)

        with open(os.path.join(mime_path, "cscript.xml"), "w") as f:
            f.write("""<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
    <mime-type type="text/x-cscript">
        <comment>CScript source file</comment>
        <glob pattern="*.cript"/>
    </mime-type>
</mime-info>""")

        # Update mime database
        os.system("update-mime-database ~/.local/share/mime")

    elif system == "Darwin":  # macOS
        # Create UTI declaration
        uti_path = os.path.expanduser("~/Library/Application Support/CScript")
        os.makedirs(uti_path, exist_ok=True)

        with open(os.path.join(uti_path, "CScript.uti"), "w") as f:
            f.write("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>UTTypeIdentifier</key>
    <string>com.cscript.source</string>
    <key>UTTypeDescription</key>
    <string>CScript Source File</string>
    <key>UTTypeConformsTo</key>
    <array>
        <string>public.source-code</string>
    </array>
    <key>UTTypeTagSpecification</key>
    <dict>
        <key>public.filename-extension</key>
        <array>
            <string>cript</string>
        </array>
    </dict>
</dict>
</plist>""")

def main():
    if len(sys.argv) < 2:
        print("Usage: cscript <filename.cript>")
        return

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return

    try:
        # Read the CScript code
        with open(filename, 'r') as file:
            content = file.read()

        # Create generator instance
        generator = MachineCodeGenerator()

        # Generate and execute code
        if generator.generate_code(content):
            print("Machine code generated successfully")
            if generator.execute_code():
                print("Code executed successfully")
            else:
                print("Error executing code")
        else:
            print("Error generating machine code")

    except Exception as e:
        print(f"Error: {str(e)}")

    # Register file extension during first run
    register_file_extension()

if __name__ == "__main__":
    main()