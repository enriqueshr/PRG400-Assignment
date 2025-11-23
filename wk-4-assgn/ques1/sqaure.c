#include <Python.h>

// Function to square an integer
static PyObject* square_square(PyObject* self, PyObject* args) {
    int x;
    if (!PyArg_ParseTuple(args, "i", &x)) {
        return NULL;
    }
    return PyLong_FromLong(x * x);
}

// Method table
static PyMethodDef SquareMethods[] = {
    {"square", square_square, METH_VARARGS, "Return the square of a number"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef squaremodule = {
    PyModuleDef_HEAD_INIT,
    "square",
    "A module for squaring numbers",
    -1,
    SquareMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_square(void) {
    return PyModule_Create(&squaremodule);
}