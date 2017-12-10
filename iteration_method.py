#%%
import numpy as np


def spectral_radius(iter_matrix):
    eigvalue, eigvector = np.linalg.eig(iter_matrix)
    return max(abs(eigvalue))


def jacobi_iteration(coe_matrix, const_col):
    size = const_col.size
    x_vector = np.zeros(const_col.size)
    xTmpVector = np.zeros(const_col.size)

    LMatrix = -1 * np.tril(coe_matrix, -1)
    UMatrix = -1 * np.triu(coe_matrix, 1)
    DMatrix = coe_matrix + LMatrix + UMatrix
    iter_matrix = (np.linalg.inv(DMatrix)).dot(LMatrix + UMatrix)
    spectral_value = spectral_radius(iter_matrix)
    if spectral_value >= 1:
        print("该矩阵不收敛！其谱半径为：{0}".format(spectral_value))
        return 1

    num=0;     
    while True:
        for i in range(size):
            tmpSum = 0
            for j in range(size):
                if i == j:
                    continue
                tmpSum = tmpSum + (coe_matrix[i][j] * x_vector[j])
            xTmpVector[i] = (const_col[i] - tmpSum) / coe_matrix[i][i]
        if sum(abs(xTmpVector - x_vector)) < 0.0001:
            break
        x_vector = np.copy(xTmpVector)
        # print("临时迭代解：{0}".format(xTmpVector))
        num=num+1;
        
    print("方程的解为：{0} ,迭代总次数为：{1},误差为0.0001".format(x_vector,num))


def G_S_Iteration(coe_matrix, const_col):
    size = const_col.size
    x_vector = np.zeros(const_col.size)
    xTmpVector = np.zeros(const_col.size)

    LMatrix = -1 * np.tril(coe_matrix, -1)
    UMatrix = -1 * np.triu(coe_matrix, 1)
    DMatrix = coe_matrix + LMatrix + UMatrix
    iter_matrix = (np.linalg.inv(DMatrix - LMatrix)).dot(UMatrix)
    spectral_value = spectral_radius(iter_matrix)
    if spectral_value >= 1:
        print("该矩阵不收敛！其谱半径为：{0}".format(spectral_value))
        return 1
    
    num=0;
    while True:
        for i in range(size):
            tmpSum1 = 0
            tmpSum2 = 0
            for j in range(i - 1):
                tmpSum1 = tmpSum1 + (coe_matrix[i][j] * xTmpVector[j])
            for j in range(i + 1, size, 1):
                tmpSum2 = tmpSum2 + (coe_matrix[i][j] * xTmpVector[j])
            xTmpVector[i] = (const_col[i] - tmpSum1 - tmpSum2) / coe_matrix[i][i]
        if sum(abs(xTmpVector - x_vector)) < 0.0001:
            break
        x_vector = np.copy(xTmpVector)
        # print("临时迭代解：{0}".format(xTmpVector))
        num=num+1;

    print("方程的解为：{0} ,迭代总次数为：{1},误差为0.0001".format(x_vector,num))

def SOR_Iteration(coe_matrix,const_col,w_factor):
    size = const_col.size
    x_vector = np.zeros(const_col.size)
    xTmpVector = np.zeros(const_col.size)

    LMatrix = -1 * np.tril(coe_matrix, -1)
    UMatrix = -1 * np.triu(coe_matrix, 1)
    DMatrix = coe_matrix + LMatrix + UMatrix
    iter_matrix = (np.linalg.inv(DMatrix -w_factor * LMatrix)).dot((1-w_factor)*DMatrix+w_factor*UMatrix)
    spectral_value = spectral_radius(iter_matrix)
    if spectral_value >= 1:
        print("该矩阵不收敛！其谱半径为：{0}".format(spectral_value))
        return 1

    num=0;
    while True:
        for i in range(size):
            tmpSum1 = 0
            tmpSum2 = 0
            for j in range(i - 1):
                tmpSum1 = tmpSum1 + (coe_matrix[i][j] * xTmpVector[j])
            for j in range(i , size, 1):
                tmpSum2 = tmpSum2 + (coe_matrix[i][j] * x_vector[j])
            xTmpVector[i] = x_vector[i] + w_factor*(const_col[i] - tmpSum1 - tmpSum2) / coe_matrix[i][i]
        if sum(abs(xTmpVector - x_vector)) < 0.000001:
            break
        x_vector = np.copy(xTmpVector)
        # print("临时迭代解：{0}".format(xTmpVector))
        num=num+1;
        

    print("方程的解为：{0},迭代总次数为：{1}".format(x_vector,num))


def main():
    coe_matrix = np.array([[1, 0.8, 0.8], [0.8, 1, 0.8], [
        0.8, 0.8, 1]], dtype=np.float)
    const_col = np.array([1, 2, 3], dtype=np.float)
    print("雅克比迭代过程：")
    jacobi_iteration(coe_matrix, const_col)
    print("\n高斯-赛德尔迭代过程：")
    G_S_Iteration(coe_matrix,const_col)

    coe_matrix1 = np.array([[4,3,0],[3,4,-1],[0,-1,4]],dtype=np.float)
    const_col1 = np.array([1,-5,3],dtype=np.float)
    
    for w_factor in [0.2,0.5,1.0,1.24,1.5,2.2]:
        print("\nw因子为：{0} 时，误差为：0.000001时的SOR迭代：".format(w_factor))
        SOR_Iteration(coe_matrix1,const_col1,w_factor)


if __name__ == '__main__':
    main()
