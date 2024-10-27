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
            REPEAT,
            VALUE,
            IDENTIFIER,
            NUMBER,
            STRING,
            OPERATOR,
            END_BLOCK
        };
        Type type;
        std::string value;

        Token(Type t, std::string v) : type(t), value(v) {}
    };

private:
  // I parser.cpp, utöka keywords:
  std::map<std::string, Token::Type> keywords = {
      // Grundläggande
      {"create", Token::CREATE},
      {"store", Token::STORE},
      {"show", Token::SHOW},

      // Matematiska operationer
      {"add", Token::MATH},
      {"subtract", Token::MATH},
      {"multiply", Token::MATH},
      {"divide", Token::MATH},
      {"power", Token::MATH},

      // Kontrollstrukturer
      {"when", Token::WHEN},
      {"otherwise", Token::OTHERWISE},
      {"repeat", Token::REPEAT},
      {"while", Token::WHILE},
      {"foreach", Token::FOREACH},

      // Listoperationer
      {"append", Token::LIST_OP},
      {"remove", Token::LIST_OP},
      {"sort", Token::LIST_OP},
      {"find", Token::LIST_OP},

      // Strängoperationer
      {"join", Token::STRING_OP},
      {"split", Token::STRING_OP},
      {"replace", Token::STRING_OP}
  };

public:
    std::vector<Token> parseCode(const std::string& code) {
        std::vector<Token> tokens;
        std::istringstream stream(code);
        std::string word;

        while (stream >> word) {
            // Check for end block
            if (word == "--") {
                tokens.emplace_back(Token::END_BLOCK, "--");
                continue;
            }

            // Check for keywords
            if (keywords.find(word) != keywords.end()) {
                tokens.emplace_back(keywords[word], word);
                continue;
            }

            // Check for operators
            if (std::find(operators.begin(), operators.end(), word) != operators.end()) {
                tokens.emplace_back(Token::OPERATOR, word);
                continue;
            }

            // Check for numbers
            if (std::all_of(word.begin(), word.end(), ::isdigit)) {
                tokens.emplace_back(Token::NUMBER, word);
                continue;
            }

            // Check for strings (with quotes)
            if (word[0] == '"' && word[word.length()-1] == '"') {
                tokens.emplace_back(Token::STRING, word.substr(1, word.length()-2));
                continue;
            }

            // Must be an identifier
            tokens.emplace_back(Token::IDENTIFIER, word);
        }

        return tokens;
    }
};

PYBIND11_MODULE(parser, m) {
    py::class_<Parser>(m, "Parser")
        .def(py::init<>())
        .def("parse_code", &Parser::parseCode);
}