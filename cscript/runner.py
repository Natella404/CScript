import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: cscript <filename.cript>")
        return

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Processing file: {filename}")
            print("CScript är redo att köra filen!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()