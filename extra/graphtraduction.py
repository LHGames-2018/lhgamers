from helper.tile import *
def translate (mat):
    # print(mat)
    graph = {}
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            graph[(mat[row][col].Position)] = neighbours(row,col,mat)
    return graph

def neighbours(row,col,mat):
    neighbours = dict()
    if(row-1 >= 0 and isValidTile(mat[row-1][col].TileContent)): 
        neighbours[(mat[row-1][col].Position)] = 1

    if(col-1 >= 0 and isValidTile(mat[row][col-1].TileContent)): 
        neighbours[(mat[row][col-1].Position)] = 1

    if(row+1 < len(mat[:]) and isValidTile(mat[row+1][col].TileContent)): 
        neighbours[(mat[row+1][col].Position)] = 1

    if(col+1 < len(mat[0]) and isValidTile(mat[row][col+1].TileContent)): 
        neighbours[(mat[row][col+1].Position)] = 1
        
    return neighbours


def isValidTile(tileContent):
    return tileContent == TileContent.Empty or tileContent == TileContent.House or tileContent == TileContent.Shop