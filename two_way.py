def two_way(matrix):
    """Computes the minimum path sum from the top left to the bottom right of a matrix 
    by only moving to the right and down"""

    n = len(matrix)
    
    #q[i][j] = minimum cost to reach (i,j) from (0,0)
    q = [[0 for c in range(n)] for r in range(n)]   #initialise q with zeros

    q[0][0] = matrix[0][0]       

    for i in range(1,n):      #sum along first column
        q[i][0] = q[i-1][0] + matrix[i][0]

    for j in range(1,n):      #sum along top row
        q[0][j] = q[0][j-1] + matrix[0][j]
    
    for i in range(1,n):
        for j in range(1,n):
            q[i][j] = matrix[i][j] + min(q[i][j-1], #approaching from left
                                         q[i-1][j]) #approaching from above

    return q[n-1][n-1]

if __name__ == '__main__':
    matrix = [[int(v) for v in line.strip().split(',')] for line in open('matrix.txt','r')]
    print(two_way(matrix))
