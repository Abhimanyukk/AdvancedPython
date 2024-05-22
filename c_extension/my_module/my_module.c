#include <Python.h>

// A simple function that adds two integers
static PyObject *my_module_add(PyObject *self, PyObject *args)
{
    int a, b;
    // Parse the input tuple
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
    {
        return NULL;
    }
    // Return the sum
    return PyLong_FromLong(a + b);
}

// Method definitions
static PyMethodDef MyModuleMethods[] = {
    {"add", my_module_add, METH_VARARGS, "Add two integers"},
    {NULL, NULL, 0, NULL}};

// Module definition
static struct PyModuleDef my_module = {
    PyModuleDef_HEAD_INIT,
    "my_module",               // Name of the module
    "A simple example module", // Module documentation
    -1,                        // Size of per-interpreter state of the module
    MyModuleMethods};

// Module initialization function
PyMODINIT_FUNC PyInit_my_module(void)
{
    return PyModule_Create(&my_module);
}
