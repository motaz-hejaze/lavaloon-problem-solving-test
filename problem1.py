print("***************** Welcome ********************")
print("calculate persistence of integers function")
print("python version 3.6+")
print("run this script to test the function by yourself")
print("or run test_problem1 for unittest script ")


counter = 0


def multiplicative_persistence(x):
    global counter
    # split string into a number list
    int_list = [int(i) for i in str(x)]
    # check if one digit only
    if len(int_list) == 1:
        result = counter
        counter = 0
        # break the recursion
        return result
    else:
        # calculate the production
        total = 1
        for i in int_list:
            total *= i
        # adding to counter this iteration
        counter += 1
        return multiplicative_persistence(total)


if __name__ == '__main__':
    x = input("Please enter a positive integer : ")
    print("persistence of {} : {}".format(x, str(multiplicative_persistence(x))))


