// cscript/core/parser.cpp
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

class Parser {
public:
    struct Token {
        enum Type {
            CREATE,
            STORE,
            SHOW,
            ARRANGE,
            WHEN,
            OTHERWISE,
            REPEAT,
            WHILE,
            FOREACH,
            VALUE,
            IDENTIFIER,
            NUMBER,
            STRING,
            OPERATOR,
            END_BLOCK,
            MATH,
            LIST_OP,
            STRING_OP
        };
        Type type;
        std::string value;

        Token(Type t, std::string v) : type(t), value(v) {}
    };

    // ... (resten av parser-koden) ...

    std::vector<std::string> parseCode(const std::string& code) {
        std::vector<std::string> result;
        std::vector<Token> tokens = tokenize(code);

        // Konvertera tokens till strings för enklare Python-integration
        for (const auto& token : tokens) {
            result.push_back(token.value);
        }

        return result;
    }

private:
    std::vector<Token> tokenize(const std::string& code) {
        // Din existerande tokenize-implementation
        std::vector<Token> tokens;
        // ... parsing logik ...
        return tokens;
    }
};

PYBIND11_MODULE(parser, m) {
    py::class_<Parser>(m, "Parser")
        .def(py::init<>())
        .def("parse_code", &Parser::parseCode);
}