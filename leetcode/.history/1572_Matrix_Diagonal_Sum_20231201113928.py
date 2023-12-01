def diagonalSum(self, mat: List[List[int]]) -> int:
    mat_sum = 0

    for i in range(len(mat)):
        primary_diagonal = mat[i][i]
        secondary_diagonal = mat[i][len(mat) - i - 1]
        mat_sum += primary_diagonal
        mat_sum += secondary_diagonal

    if len(mat) % 2 != 0:
        mid_point_num = len(mat) // 2
        mid_point = mat[mid_point_num][mid_point_num]
        mat_sum -= mid_point

    return mat_sum
