import math

def sigma(num):
    if num > 0:
        num += int( sigma(num-1) )
    else:
        return 0
    
    return math.trunc(num)

# print( sigma(5) )
# print( sigma(2.5) )
# print( sigma(-1) )


def factorial(num):
    num = math.trunc(num)


    if num > 1:
        num *= factorial(num-1)
    else:
        return 1

    return num

# print( factorial(0) )
# print( factorial(3) )
# print( factorial(6.5) )


def flood_fill(arr, start_YX, newColor):
    
    #If current location is not newColor
    try:
        old_color = arr[start_YX[0]][start_YX[1]]
        if arr[start_YX[0]][start_YX[1]] != newColor:
            arr[start_YX[0]][start_YX[1]] = newColor
        else:
            return 0
    except:
        return 0

    #Send function in all 4 directions
    try:
        if arr[start_YX[0]+1][start_YX[1]] == old_color:
            flood_fill(arr, [ start_YX[0]+1, start_YX[1] ], newColor)
    except:
        pass
    
    try:
        if arr[start_YX[0]-1][start_YX[1]] == old_color:
            flood_fill(arr, [ start_YX[0]-1, start_YX[1] ], newColor)
    except:
        pass
    
    try:
        if arr[start_YX[0]][start_YX[1]+1] == old_color:
            flood_fill(arr, [ start_YX[0], start_YX[1]+1 ], newColor)
    except:
        pass

    try:
        if arr[start_YX[0]][start_YX[1]-1] == old_color:
            flood_fill(arr, [ start_YX[0], start_YX[1]-1 ], newColor)
    except:
        pass


def print_array(arr):
    for i in range( len(arr) ):
        output = ""
        for j in range( len(arr[i]) ):
            output += str(arr[i][j])
        print(output)
    print(" ")


test_arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
flood_fill(test_arr, [2,2], 2)
print_array(test_arr)


test_arr = [
    [0,1,0,0,0],
    [1,1,0,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
]
flood_fill(test_arr, [2,2], 2)
print_array(test_arr)


test_arr = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1],
]
flood_fill(test_arr, [2,2], 2)
print_array(test_arr)
