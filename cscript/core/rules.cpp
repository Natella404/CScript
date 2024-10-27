// cscript/core/rules.cpp
#include <string>
#include <vector>
#include <map>
#include <functional>
#include <pybind11/pybind11.h>
#include "parser.cpp"

namespace py = pybind11;

class RuleEngine {
private:
    struct Rule {
        std::string pattern;
        std::vector<std::string> requiredTokens;
        std::function<std::string(const std::vector<Parser::Token>&)> generator;
    };

    std::map<Parser::Token::Type, std::vector<Rule>> rules;

public:
    RuleEngine() {
        initializeRules();
    }

    std::string applyRules(const std::vector<Parser::Token>& tokens) {
        std::string machineCode;

        for (size_t i = 0; i < tokens.size(); i++) {
            const auto& token = tokens[i];

            // Hitta matchande regler för token-typen
            if (rules.find(token.type) != rules.end()) {
                for (const auto& rule : rules[token.type]) {
                    // Kontrollera om regeln matchar
                    if (matchesPattern(tokens, i, rule)) {
                        // Generera optimerad maskinkod
                        machineCode += rule.generator(
                            std::vector<Parser::Token>(
                                tokens.begin() + i,
                                tokens.begin() + i + rule.requiredTokens.size()
                            )
                        );

                        // Hoppa över tokens som använts
                        i += rule.requiredTokens.size() - 1;
                        break;
                    }
                }
            }
        }

        return machineCode;
    }

private:
    void initializeRules() {
        // CREATE regler
        rules[Parser::Token::CREATE] = {
            {
                "create variable",
                {"create", "identifier"},
                [](const auto& tokens) {
                    return "ALLOC " + tokens[1].value + "\n";
                }
            },
            {
                "create list",
                {"create", "list", "identifier"},
                [](const auto& tokens) {
                    return "ALLOC_ARRAY " + tokens[2].value + "\n";
                }
            }
        };

        // STORE regler
        rules[Parser::Token::STORE] = {
            {
                "store value",
                {"store", "value"},
                [](const auto& tokens) {
                    return "STORE_VALUE " + tokens[1].value + "\n";
                }
            },
            {
                "store calculation",
                {"store", "calculation"},
                [](const auto& tokens) {
                    return "CALC_AND_STORE " + tokens[1].value + "\n";
                }
            }
        };

        // WHEN regler
        rules[Parser::Token::WHEN] = {
            {
                "when condition",
                {"when", "condition"},
                [](const auto& tokens) {
                    return "IF_CHECK " + tokens[1].value + "\n";
                }
            }
        };

        // REPEAT regler
        rules[Parser::Token::REPEAT] = {
            {
                "repeat times",
                {"repeat", "number", "times"},
                [](const auto& tokens) {
                    return "LOOP_START " + tokens[1].value + "\n";
                }
            }
        };
    }

    bool matchesPattern(const std::vector<Parser::Token>& tokens, 
                       size_t startIndex, 
                       const Rule& rule) {
        if (startIndex + rule.requiredTokens.size() > tokens.size()) {
            return false;
        }

        for (size_t i = 0; i < rule.requiredTokens.size(); i++) {
            if (tokens[startIndex + i].value != rule.requiredTokens[i]) {
                return false;
            }
        }

        return true;
    }
};

PYBIND11_MODULE(rules, m) {
    py::class_<RuleEngine>(m, "RuleEngine")
        .def(py::init<>())
        .def("apply_rules", &RuleEngine::applyRules);
}