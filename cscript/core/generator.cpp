// cscript/core/generator.cpp
#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <memory>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

// Definiera klassen utanför PYBIND11_MODULE
class MachineCodeGenerator {
private:
    std::vector<std::string> machineCode;
    std::map<std::string, int> variables;

public:
    MachineCodeGenerator() {}

    std::vector<std::string> generateMachineCode(const std::vector<std::string>& tokens) {
        machineCode.clear();
        variables.clear();

        for (const auto& token : tokens) {
            machineCode.push_back("Processing: " + token);
        }

        return machineCode;
    }

    bool executeCode(const std::vector<std::string>& code) {
        try {
            for (const auto& instruction : code) {
                std::cout << instruction << std::endl;
            }
            return true;
        } catch (const std::exception& e) {
            std::cerr << e.what() << std::endl;
            return false;
        }
    }
};

// Definiera PYBIND11_MODULE separat
PYBIND11_MODULE(generator, m) {
    m.doc() = "CScript code generator module"; // Optional dokumentation

    py::class_<MachineCodeGenerator>(m, "MachineCodeGenerator")
        .def(py::init<>())
        .def("generate_machine_code", &MachineCodeGenerator::generateMachineCode)
        .def("execute_code", &MachineCodeGenerator::executeCode);
}