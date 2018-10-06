from helper.tile import *
def translate (mat):
    graph = {}
    for col in range(len(mat[:])):
        for row in range(len(mat[col])):
            if isValidTile(mat[row][col]):
                graph["{},{}".format(row,col)] = neighbours(row,col,mat)
    return graph

def neighbours(row,col,mat):
    neighbours = []
    if(row-1 >= 0 and isValidTile(mat[row-1][col])): 
        neighbours.append("{},{}".format(row-1,col))

    if(col-1 >= 0 and isValidTile(mat[row][col-1])): 
        neighbours.append("{},{}".format(row,col-1))

    if(row+1 < len(mat[:]) and isValidTile(mat[row+1][col])): 
        neighbours.append("{},{}".format(row+1,col))

    if(col+1 < len(mat[0]) and isValidTile(mat[row][col+1])): 
        neighbours.append("{},{}".format(row,col+1))
        
    return neighbours


def isValidTile(tileContent):
    return tileContent == TileContent.Empty or tileContent == TileContent.House or tileContent == TileContent.Shop