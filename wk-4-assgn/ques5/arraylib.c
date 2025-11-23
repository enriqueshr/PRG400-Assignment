#include <Python.h>
#include <stdlib.h>

// Struct to hold the array
typedef struct {
    PyObject_HEAD
    int* data;
    size_t size;
} ArrayObject;

// Deallocate the array
static void Array_dealloc(ArrayObject* self) {
    free(self->data);
    Py_TYPE(self)->tp_free((PyObject*)self);
}

// Initialize the array with a given size
static PyObject* Array_init(ArrayObject* self, PyObject* args) {
    size_t size;
    if (!PyArg_ParseTuple(args, "n", &size)) {
        return NULL;
    }
    self->data = (int*)malloc(size * sizeof(int));
    if (!self->data) {
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory");
        return NULL;
    }
    self->size = size;
    Py_RETURN_NONE;
}

// Set a value at an index
static PyObject* Array_set(ArrayObject* self, PyObject* args) {
    size_t index;
    int value;
    if (!PyArg_ParseTuple(args, "ni", &index, &value)) {
        return NULL;
    }
    if (index >= self->size) {
        PyErr_SetString(PyExc_IndexError, "Index out of range");
        return NULL;
    }
    self->data[index] = value;
    Py_RETURN_NONE;
}

// Get a value at an index
static PyObject* Array_get(ArrayObject* self, PyObject* args) {
    size_t index;
    if (!PyArg_ParseTuple(args, "n", &index)) {
        return NULL;
    }
    if (index >= self->size) {
        PyErr_SetString(PyExc_IndexError, "Index out of range");
        return NULL;
    }
    return PyLong_FromLong(self->data[index]);
}

// Free the array (manual free, though dealloc handles it)
static PyObject* Array_free(ArrayObject* self, PyObject* args) {
    free(self->data);
    self->data = NULL;
    self->size = 0;
    Py_RETURN_NONE;
}

// Method table
static PyMethodDef Array_methods[] = {
    {"init", (PyCFunction)Array_init, METH_VARARGS, "Initialize array with size"},
    {"set", (PyCFunction)Array_set, METH_VARARGS, "Set value at index"},
    {"get", (PyCFunction)Array_get, METH_VARARGS, "Get value at index"},
    {"free", (PyCFunction)Array_free, METH_VARARGS, "Free the array"},
    {NULL}
};

// Type definition
static PyTypeObject ArrayType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "arraylib.Array",             /* tp_name */
    sizeof(ArrayObject),          /* tp_basicsize */
    0,                            /* tp_itemsize */
    (destructor)Array_dealloc,    /* tp_dealloc */
    0,                            /* tp_print */
    0,                            /* tp_getattr */
    0,                            /* tp_setattr */
    0,                            /* tp_as_async */
    0,                            /* tp_repr */
    0,                            /* tp_as_number */
    0,                            /* tp_as_sequence */
    0,                            /* tp_as_mapping */
    0,                            /* tp_hash */
    0,                            /* tp_call */
    0,                            /* tp_str */
    0,                            /* tp_getattro */
    0,                            /* tp_setattro */
    0,                            /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,           /* tp_flags */
    "Array object",               /* tp_doc */
    0,                            /* tp_traverse */
    0,                            /* tp_clear */
    0,                            /* tp_richcompare */
    0,                            /* tp_weaklistoffset */
    0,                            /* tp_iter */
    0,                            /* tp_iternext */
    Array_methods,                /* tp_methods */
    0,                            /* tp_members */
    0,                            /* tp_getset */
    0,                            /* tp_base */
    0,                            /* tp_dict */
    0,                            /* tp_descr_get */
    0,                            /* tp_descr_set */
    0,                            /* tp_dictoffset */
    0,                            /* tp_init */
    0,                            /* tp_alloc */
    PyType_GenericNew,            /* tp_new */
};

// Module initialization
static PyModuleDef arraylibmodule = {
    PyModuleDef_HEAD_INIT,
    "arraylib",
    "A module for managing integer arrays",
    -1,
    NULL
};

PyMODINIT_FUNC PyInit_arraylib(void) {
    PyObject* m;
    if (PyType_Ready(&ArrayType) < 0) return NULL;
    m = PyModule_Create(&arraylibmodule);
    if (m == NULL) return NULL;
    Py_INCREF(&ArrayType);
    PyModule_AddObject(m, "Array", (PyObject*)&ArrayType);
    return m;
}