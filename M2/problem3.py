a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result
    emptyArr = []
    for i in arr:
        if (float(i) > 0) and (isinstance(i, str) == False):
            emptyArr.append(i)
        elif (isinstance(i, str) == True):
            if (float(i) > 0):
                emptyArr.append(i)
            elif (float(i) < 0):
                new_i = abs(int(i))
                str_i = str(new_i)
                emptyArr.append(str_i)
        elif (float(i) < 0) and (isinstance(i, str) == False):
            emptyArr.append(abs((i)))

    print(emptyArr)
    for i in emptyArr:
        print(type(i), end=" , ")


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
