class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows,cols = len(mat),len(mat[0])
        o = r * c
        if rows*cols != o:
            return mat
        new_matrix = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(o):
            new_matrix[i//c][i%c] = mat[i//cols][i%cols]
        return new_matrix