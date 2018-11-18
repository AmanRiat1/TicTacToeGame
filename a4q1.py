def add(matrix):
    '''(list) -> (list)
    * Modifies array to add 1 to each element
    * Preconditions: matrix is a reference to user inputed array
    '''
    print("The input array is:", matrix)

    
    numRows = len(matrix)
    numCol = len(matrix[0])

    result = [[0 for x in range(numCol)] for y in range(numRows)]
    #iterating through array and adding 1
    for i in range (numRows):
        for j in range (numCol):
            result[i][j] = matrix[i][j] + 1
    matrix = result
    print("After executing the function add, the array is:",matrix)
    return matrix


def add_V2(y):
    '''(List) -> (list)
    * Creates new array with each element in original array increased by 1
    * Preconditions: y is a reference to user inputted array

    '''
    new = y.copy()
    a = []
    z = (len(y))
    for d in range(0,z):
        #Adds 1 to each element in array position new[d]
        b = [a + 1 for a in new[d]]
        a.append(b)
    print("A new array created with add_V2:",a)
    print("After executing the function add_V2, the initial array is:",y)

####
'''
For input below, enter rows wanted, then array elements. Ex.

Rows wanted: 2
1 2 3
4 5 6

Then array is taken as [[1,2,3],[4,5,6]]
'''
###

m = int(input("Input the rows wanted. Then enter rows with array elements followed by spaces: "))
input_matrix = []
i = 0
while (i < m):
    row = [int(val) for val in input().split()]
    input_matrix.append(row)
    i = i + 1



input_matrix = add(input_matrix)
add_V2(input_matrix)

