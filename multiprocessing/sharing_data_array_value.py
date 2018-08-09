import multiprocessing

def square_list(mylist, result, square_sum):

    for idx, num in enumerate(mylist):
        result[idx] = num * num

    square_sum.value = sum(result)

    print(f"Result(in process p1): {result[:]}")

    print(f"Sum of squares(in process p1): {square_sum.value}")

if __name__ == "__main__":
    mylist = [1,2,3,4]

    # creating Array of int data type with space for 4 integers
    result = multiprocessing.Array('i', 4)

    # creating Value of int data type
    square_sum = multiprocessing.Value('i')

    # creating new process
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

    # starting process
    p1.start()

    # wait until process is finished
    p1.join()

    # print result array
    print(f"Result(in main program): {result[:]}")

    # print square_sum Value
    print(f"Sum of squares(in main program):  {square_sum.value}")
