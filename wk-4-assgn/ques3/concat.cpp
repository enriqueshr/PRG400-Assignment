#include <pybind11/pybind11.h>
#include <string>

std::string concatenate(const std::string& a, const std::string& b) {
    return a + b;
}

PYBIND11_MODULE(concat, m) {
    m.def("concatenate", &concatenate, "Concatenate two strings");
}