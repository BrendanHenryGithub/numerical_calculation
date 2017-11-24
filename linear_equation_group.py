#%%
import numpy as np

def matrix_decomposition(augMatrix):
    row,col=augMatrix.shape
    for r in range (row):
        tmpSum=0
        for k in range(0,r,1):
            tmpSum=tmpSum+augMatrix[r,k]*augMatrix[k,r]
        augMatrix[r,r]=augMatrix[r,r]-tmpSum
        s=augMatrix[r,r]
        sMax=abs(s)
        rowNum=r
        for i in range(r+1,row,1):
            tmpSum=0
            for k in range(0,r,1):
                tmpSum=tmpSum+augMatrix[i,k]*augMatrix[k,r]
            augMatrix[i,r]=augMatrix[i,r]-tmpSum
            s=abs(augMatrix[i,r])
            if s>sMax:
                sMax=s
                rowNum=i
        if rowNum!=r:
           augMatrix[[r, rowNum], :] = augMatrix[[rowNum, r], :] 
        for i in range(r+1,row,1):
            if r!=row-1:
                augMatrix[i,r]=augMatrix[i,r]/augMatrix[r,r]
                tmpSum=0
                for k in range(0,r,1):
                    tmpSum=tmpSum+augMatrix[r,k]*augMatrix[k,i]
                augMatrix[r,i]=augMatrix[r,i]-tmpSum

    for i in range(1,row,1):
        tmpSum=0
        for k in range(0,i,1):
            tmpSum=tmpSum+augMatrix[i,k]*augMatrix[k,col-1]
        augMatrix[i,col-1]=augMatrix[i,col-1]-tmpSum

    augMatrix[row-1,col-1]=augMatrix[row-1,col-1]/augMatrix[row-1,row-1]
    for i in range(row-2,-1,-1):
        tmpSum=0
        for k in range(i+1,row,1):
            tmpSum=tmpSum+augMatrix[i,k]*augMatrix[k,col-1]
        augMatrix[i,col-1]=(augMatrix[i,col-1]-tmpSum)/augMatrix[i,i]
    print(augMatrix)
    return 0



def gauss_column_elimination(augMatrix):
    det = 1
    row, col = augMatrix.shape
    for i in range(row - 1):
        colMaxNum = i
        for rowNum in range(i, row):
            if abs(augMatrix[rowNum, i]) > abs(augMatrix[i, i]):
                colMaxNum = rowNum
        if augMatrix[colMaxNum, i] == 0:
            det = 0
            print("矩阵的det=0!")
            return 1
        if colMaxNum != i:
            augMatrix[[i, colMaxNum], :] = augMatrix[[colMaxNum, i], :]
            det = det * (-1)
        for rowNum in range(i + 1, row):
            augMatrix[rowNum, i] = augMatrix[rowNum, i] / augMatrix[i, i]
            for colNum in range(i + 1, col):
                augMatrix[rowNum, colNum] = augMatrix[rowNum, colNum] - \
                    augMatrix[rowNum, i] * augMatrix[i, colNum]
        det = det * augMatrix[i, i]
    if augMatrix[row - 1, row - 1] == 0:
        det = 0
        print("矩阵的det=0!")
        return 1
    det = det * augMatrix[row - 1, row - 1]
    print("矩阵的det={0:.2f}".format(det))
    for i in range(row - 1, -1, -1):
        tmpSum = 0
        for j in range(i + 1, row, 1):
            tmpSum = tmpSum + augMatrix[j, col - 1] * augMatrix[i, j]
        augMatrix[i, col - 1] = (augMatrix[i, col - 1] - tmpSum) / augMatrix[i, i]
    for i in range(row):
        print("x[{0}]={1:.2f}".format(i + 1, augMatrix[i, col - 1]))
    return 0

def main():
    coeMatrix = np.array([[10, -7, 0,1], [-3, 2.099999, 6,2], [5, -1, 5,-1],[2,1,0,2]],dtype=np.float)
    constCol = np.array([[8], [5.900001], [5],[1]],dtype=np.float)
    e=np.concatenate((coeMatrix, constCol), axis=1)
    d=np.copy(e)
    np.set_printoptions(precision=6, suppress=True)
    print("增广矩阵为：\n{0}".format(e))
    print("高斯列选主元消去法：")
    gauss_column_elimination(e)
    print("矩阵三角选主元分解法：")
    matrix_decomposition(d)
    return 0

if __name__ == '__main__':
    main()

# result:
# 增广矩阵为：
# [[ 10.        -7.         0.         1.         8.      ]
#  [ -3.         2.099999   6.         2.         5.900001]
#  [  5.        -1.         5.        -1.         5.      ]
#  [  2.         1.         0.         2.         1.      ]]
# 高斯列选主元消去法：
# 矩阵的det=-762.00
# x[1]=0.00
# x[2]=-1.00
# x[3]=1.00
# x[4]=1.00
# 矩阵三角选主元分解法：
# [[ 10.        -7.         0.         1.        -0.      ]
#  [  0.5        2.5        5.        -1.5       -1.      ]
#  [ -0.3       -0.         6.000002   2.299999   1.      ]
#  [  0.2        0.96      -0.8        5.079999   1.      ]]