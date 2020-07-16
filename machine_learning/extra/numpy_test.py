import numpy as np


def ndarray_integer_arange(min_value, max_value, step_value):
    """max_value is not include in array"""
    return np.arange(min_value, max_value, step_value)


def ndarray_float_arange(min_value, max_value, split_number):
    """max_value is include in array"""
    return np.linspace(min_value, max_value, split_number)


def n_dimensional_zero_array(*array_shape):
    """generate n-dimensional array with number zero\r\n
    eg.
        one dimensional :    n_dimensional_zero_array(2)\r\n
        two dimensional :    n_dimensional_zero_array(2,2))\r\n
        three dimensional:    n_dimensional_zero_array(2,3,4))
    """
    return np.zeros(array_shape)


def n_dimensional_one_array(*array_shape):
    """generate n-dimensional array with number one"""
    return np.ones(array_shape)


def n_dimensional_array_full_number(full_number, *array_shape):
    """generate n-dimensional array with with the given value\r\n
        eg. n_dimensional_array_full_number(np.pi, 3, 4), this create 3x4 matrix full of π
    """
    return np.full(array_shape, full_number)


def n_dimensional_array_random_number(*array_shape):
    """random_sample, function equals rand, unlike rand, can accept a tuple as argument """
    return np.random.random_sample(array_shape)


def n_dimensional_array_random_number_normal(*array_shape):
    """standard_normal, function equals randn, unlike randn, can accept a tuple as argument\r\n
     return random number in normal distribution (Gaussian distribution)
     """
    return np.random.standard_normal(array_shape)


def get_array_rank(array):
    """equal to len(numpy.shape)"""
    return np.ndim(array)


def get_array_shape(array):
    """get an array's list of axis lengths
     , rank is equal to the shape's length."""
    return np.shape(array)


def get_array_size(array):
    """the total number of elements,
    which is the product of all axis lengths (eg. 3*4=12)"""
    return np.size(array)


def get_array_universal_functions(array, np_function_name):
    for func in (np.min, np.max, np.sum, np.std, np.var, np.mean, np.prod, np.square, np.abs,
                 np.sqrt, np.exp, np.log, np.sign, np.ceil, np.modf, np.isnan, np.cos):
        if func.__name__ == np_function_name:
            return func(array)


def save_numpy_array(file_name, file_type, array):
    if file_type is None:
       np.save(file_name, array)
    elif file_type == 'text':
       np.savetxt(''.join((file_name, '.csv')), array, delimiter=',')


def save_zipped_numpy_array(file_name, compress, array):
    if compress is False:
        np.savez(file_name, array)
    else:
        np.savez_compressed(file_name, array)


def load_numpy_array(file_name, file_type):
    if file_type is None:
        return np.load(''.join((file_name, '.npy')))
    elif file_type == 'text':
        return np.loadtxt(''.join((file_name, '.csv')), delimiter=',')


def load_zipped_numpy_array(file_name):
    return np.load(''.join((file_name, '.npz'))).get('arr_0')


# print(get_array_shape(two_rank_dimensional(4, 2)))
# print(get_array_size(two_rank_dimensional(4, 2)))
# print(get_array_rank(two_rank_dimensional(4, 2)))
# print(ndarray_integer_arange(0, 5/3, 5/9))
# print(ndarray_float_arange(0, 5/3, 4))
# print(n_dimensional_array_random_number(2, 3))
# print(n_dimensional_array_random_number_normal(2, 3))
# a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])
# print(get_array_universal_functions(a, 'cos'))
