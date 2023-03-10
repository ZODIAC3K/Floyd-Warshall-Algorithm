import math
# Floyd Algorithm in python.
x = 9
INF = math.inf

# Algorithm implementation
def floyd_algo(arr):
    # Adding vertices individually
    for k in range(x):
        print("")
        print("D[",k,"]")
        print("")
        for i in range(x):
            for j in range(x):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
                if(arr[i][j] == INF):
                    print("INF", end="\t")
                else:
                    print(arr[i][j], end="\t")
            print("")
        print("")
    print("")
    print("-- INPUT --")
    print("")
    print_input(arr)
    print("")
    print("-- OUTPUT --")
    print("")
    print_solution(arr)

# Printing the solution
def print_solution(arr):
    for i in range(x):
        for j in range(x):
            if(arr[i][j] == INF):
                print("INF", end="\t ")
            else:
                print(arr[i][j], end="\t  ")
        print("")


def print_input(arr):
    for i in range(x):
        for j in range(x):
            if(arr[i][j] == INF):
                print("INF", end="\t")
            else:
                print(arr[i][j], end="\t")
        print(" ")


arr = [
        [0, 4, INF, INF, INF, INF, INF, 8, INF],
        [4, 0, 8, INF, INF, INF, INF, 11, INF],
        [INF, 8, 0, 7, INF, INF, INF, INF, 2],
        [INF, INF, 7, 0, 9, 14, INF, INF, INF],
        [INF, INF, INF, 9, 0, 10, INF, INF, INF],
        [INF, INF, 4, 14, 10, 0, 2, INF, INF],
        [INF, INF, INF, INF, INF, 2, 0, 1, 6],
        [8, 11, INF, INF, INF, INF, 1, 0, INF],
        [INF, INF, 2, INF, INF, INF, 6, 7, 0]
    ]

floyd_algo(arr)