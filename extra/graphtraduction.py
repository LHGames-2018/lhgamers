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
        if mat[row-1][col].TileContent == TileContent.Wall:
            weight = 3
        else:
            weight = 1
        neighbours[(mat[row-1][col].Position)] = weight

    if(col-1 >= 0 and isValidTile(mat[row][col-1].TileContent)): 
        if mat[row][col-1].TileContent == TileContent.Wall:
            weight = 3
        else:
            weight = 1
        neighbours[(mat[row][col-1].Position)] = weight

    if(row+1 < len(mat[:]) and isValidTile(mat[row+1][col].TileContent)): 
        if mat[row+1][col].TileContent == TileContent.Wall:
            weight = 3
        else:
            weight = 1
        neighbours[(mat[row+1][col].Position)] = weight

    if(col+1 < len(mat[0]) and isValidTile(mat[row][col+1].TileContent)): 
        if mat[row][col+1].TileContent == TileContent.Wall:
            weight = 3
        else:
            weight = 1
        neighbours[(mat[row][col+1].Position)] = weight
        
    return neighbours


def isValidTile(tileContent):
    return tileContent == TileContent.Empty or tileContent == TileContent.Shop or tileContent == TileContent.Wall or tileContent == TileContent.Resource