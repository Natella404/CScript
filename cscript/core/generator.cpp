// cscript/core/generator.cpp
#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <memory>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

class MachineCodeGenerator {  // Notera: Detta är klassens exakta namn
private:
    // ... (tidigare kod) ...

public:
    MachineCodeGenerator() {}  // Explicit konstruktor

    std::vector<std::string> generateMachineCode(const std::vector<std::string>& tokens) {
        // ... (tidigare kod) ...
        return machineCode;
    }

    bool executeCode(const std::vector<std::string>& machineCode) {
        // ... (tidigare kod) ...
        return true;
    }
};

PYBIND11_MODULE(generator, m) {
    py::class_<MachineCodeGenerator>(m, "MachineCodeGenerator")
        .def(py::init<>())
        .def("generate_machine_code", &MachineCodeGenerator::generateMachineCode)
        .def("execute_code", &MachineCodeGenerator::executeCode);
}