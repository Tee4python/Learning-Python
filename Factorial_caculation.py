def FirstFactorial_2(num):
    x = 1
    if num < 0:
        return "Invalid request"
    else:
        for index in range(num, 1, -2):

            """# num is the start point variable, 1 is the stop point i.e. it will stop at index 2 because python 
            numbering always start from 0, -2 is a step point i.e. The execution will skip the last two indexes and 
            its calculation from the back, thereafter compute other values after the last two indexes that was 
            skipped. If -1 is used as step point, it will reach the last index & stop because -1 stand for the last 
            element or index in a list e.g. [ 0:-1] via list slicing method i.e. Lst[Initial : End : IndexJump] """

            print(index)  # printing human-readable process of the index on the console

            x = x * index  # Function to be performed within the "for" loop

            print(x)  # printing human-readable process of the function on the console

        # return f'{x}'  # returning the exact result that the function performed at the background.


if __name__ == '__main__':
    print(FirstFactorial_2(5))  # % is the value of the num variable provided


"""" Explanation of the function"""

"""In the "for" loop, our each index will be = 5, 4, 3, 2, 1 i.e. equal to the value of "num" provided. Thereafter, 
the function will take each index and multiply it with the each corresponding value of the index that follows until it 
reached the declared stop point e.g. 

# Assuming the stop point =  1, and step point = -2
5*3 = 15  # function will skip indexes 5, 4 from the back and compute starting from index 3 then stop at index 1

# Assuming the stop point = 1, and step point = -1
5x4 = 20  # Starting from 5 i.e. the value of num provided
20*3 = 60  # result of the 1st * the next index
60*2 = 120  # result of the 2nd * the next index, which equals the stop point declared

# Assuming the stop point = 0, and step point = -1
5x4 = 20  # Starting from 5 i.e. the value of num provided
20*3 = 60  # result of the 1st * the next index
60*2 = 120  # result of the 2nd * the next index
120*1 = 120  # result of the 3rd * the next index, which equals the stop point declared

Assuming the stop point =  1, and step point = -3
5*2 = 10  # function will skip indexes 5, 4, 3 from the back and compute starting from index 2 then stop at index 1

"""


def FirstFactorial(num):
    x = 1

    if num < 0:
        return "Invalid request"
    elif num < 2:
        return '{}! = {}'.format(num, x)
    else:
        for i in range(num, 1, -1):
            x = x * i
        return '{}'.format(x)

# print(FirstFactorial(3))
