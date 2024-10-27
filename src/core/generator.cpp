#include <iostream>
#include <vector>
#include <string>

class CodeGenerator {
public:
    void generateMachineCode(const std::vector<std::string>& rules) {
        for (const auto& rule : rules) {
            processRule(rule);
        }
    }

private:
    void processRule(const std::string& rule) {
        // Här kommer logiken för att generera maskinkod
    }
};