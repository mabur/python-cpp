#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <algorithm>
#include <functional>

namespace py = pybind11;

const auto make_predicate(py::function f) {
    return [=](const auto& input) -> bool
    {
        return py::object{f(input)}.cast<bool>();
    };
};

int len(py::object x){
    if (py::isinstance<py::array>(x))
        return x.cast<py::array>().request().size;
    if (py::isinstance<py::sequence>(x))
        return x.cast<py::sequence>().size();
    if (py::isinstance<py::iterable>(x))
        return std::distance(x.begin(), x.end());
}

int count(py::iterable x, py::object y){
    return std::count(x.begin(), x.end(), y);
}

int count_if(py::iterable x, py::function f){
    return std::count_if(x.begin(), x.end(), make_predicate(f));
}

void fill(py::list x, py::object y){
    for (auto i = 0; i < x.size(); ++i){
        x[i] = y;
    }
}


void add(py::sequence left, py::sequence right, py::list out){
    const size_t num_elements = left.size();
    for (size_t i = 0; i < num_elements; ++i){
        out[i] = left[i] + right[i];
    }
}


template<typename T>
void fill_array_template(py::array_t<T> x, py::object y) {
    const auto info  = x.request();
    const auto first = static_cast<T*>(info.ptr);
    const auto last  = first + info.size;
    const auto value = y.cast<T>();
    std::fill(first, last, value);
}

void fill_i32(py::array x, py::object y) {
    fill_array_template<std::int64_t>(x, y);
}

PYBIND11_MODULE(python_example, m) {
    m.def("len", &len);
    m.def("count", &count);
    m.def("count_if", &count_if);
    m.def("fill", &fill);
    m.def("fill_i32", &fill_i32);
    m.def("add", &add);
}
