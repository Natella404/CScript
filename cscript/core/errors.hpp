// cscript/core/errors.hpp
#pragma once
#include <string>
#include <stdexcept>

namespace CScript {
    // Interna kompileringsfel
    class InternalError : public std::runtime_error {
    public:
        InternalError(const std::string& message) 
            : std::runtime_error("INTERNAL ERROR: " + message) {}
    };

    // Användarens syntaxfel
    class SyntaxError : public std::runtime_error {
    public:
        SyntaxError(const std::string& message, int line = -1) 
            : std::runtime_error(formatError(message, line)) {}

    private:
        static std::string formatError(const std::string& message, int line) {
            if (line == -1) {
                return "SYNTAX ERROR: " + message;
            }
            return "SYNTAX ERROR at line " + std::to_string(line) + ": " + message;
        }
    };
}

// cscript/core/parser.cpp
void Parser::parseCode(const std::string& code) {
    try {
        // Parsing kod här
        if (syntaxError) {
            throw CScript::SyntaxError("Invalid syntax in script", lineNumber);
        }
    } catch (const std::exception& e) {
        if (dynamic_cast<const CScript::SyntaxError*>(&e)) {
            // Användarfel - visa vänligt felmeddelande
            std::cerr << e.what() << "\n";
            std::cerr << "Try checking your CScript syntax.\n";
        } else {
            // Internt fel - visa tekniskt felmeddelande
            std::cerr << "An internal compiler error occurred.\n";
            std::cerr << "Please report this bug: " << e.what() << "\n";
        }
        throw;
    }
}

// cscript/runner.py
def main():
    try:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            content = file.read()

        try:
            parser = Parser()
            generator = MachineCodeGenerator()

            tokens = parser.parse_code(content)
            machine_code = generator.generate_machine_code(tokens)

        except RuntimeError as e:
            error_msg = str(e)
            if "SYNTAX ERROR" in error_msg:
                print("\033[91m" + error_msg + "\033[0m")  # Röd text för syntaxfel
                print("Check your CScript syntax in", filename)
            else:
                print("\033[93m" + "Internal compiler error:" + "\033[0m")  # Gul text för interna fel
                print(error_msg)
                print("Please report this bug!")
            sys.exit(1)

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)