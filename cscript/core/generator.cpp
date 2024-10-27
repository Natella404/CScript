// cscript/core/generator.cpp
#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <memory>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

class MachineCodeGenerator {
private:
    std::vector<std::string> machineCode;  // Lagt till denna rad
    std::map<std::string, int> variables;

public:
    MachineCodeGenerator() {}

    std::vector<std::string> generateMachineCode(const std::vector<std::string>& tokens) {
        // Rensa tidigare genererad kod
        machineCode.clear();
        variables.clear();

        // Här kommer vi senare implementera den faktiska kodgenereringen
        for (const auto& token : tokens) {
            machineCode.push_back("Processing: " + token);
        }

        return machineCode;
    }

    bool executeCode(const std::vector<std::string>& code) {
        try {
            for (const auto& instruction : code) {
                std::cout << "Executing: " << instruction << std::endl;
            }
            return true;
        } catch (const std::exception& e) {
            std::cerr << "Execution error: " << e.what() << std::endl;
            return false;
        }
    }
};

PYBIND11_MODULE(generator, m) {
    py::class_<MachineCodeGenerator>(m, "MachineCodeGenerator")
        .def(py::init<>())
        .def("generate_machine_code", &MachineCodeGenerator::generateMachineCode)
        .def("execute_code", &MachineCodeGenerator::executeCode);
}