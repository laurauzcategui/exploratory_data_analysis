# Use the numpy library
import numpy as np


def prepare_inputs(inputs):
    # TODO: create a 2-dimensional ndarray from the given 1-dimensional list;
    #       assign it to input_array
    input_array = np.array([inputs])

    # TODO: find the minimum value in input_array and subtract that
    #       value from all the elements of input_array. Store the
    #       result in inputs_minus_min
    inputs_minus_min = input_array - input_array.min()

    # TODO: find the maximum value in inputs_minus_min and divide
    #       all of the values in inputs_minus_min by the maximum value.
    #       Store the results in inputs_div_max.
    maxi = inputs_minus_min.max()
    inputs_div_max = inputs_minus_min / maxi

    # return the three arrays we've created
    return input_array, inputs_minus_min, inputs_div_max


def multiply_inputs(m1, m2):
    # TODO: Check the shapes of the matrices m1 and m2.
    #       m1 and m2 will be ndarray objects.
    #
    #       Return False if the shapes cannot be used for matrix
    #       multiplication. You may not use a transpose
    shape_m1 = np.shape(m1)
    shape_m2 = np.shape(m2)
    if shape_m1[1] == shape_m2[0]:
        return np.matmul(m1,m2)
    elif shape_m1[0] == shape_m2[1]:
        return np.matmul(m2,m1)
    else:
        return False


def find_mean(values):
    # TODO: Return the average of the values in the given Python list
    return np.average(values)


input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1,2,7])
print("Input as Array: {}".format(input_array))
print("Input minus min: {}".format(inputs_minus_min))
print("Input  Array: {}".format(inputs_div_max))

print("Multiply 1:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3],[4]]))))
print("Multiply 2:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3]]))))
print("Multiply 3:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1,2]]))))

print("Mean == {}".format(find_mean([1,3,4])))
