class Solution {
    public int[][] generateMatrix(int n) {

        int[][] matrix = new int[n][n];

        int srow = 0, erow = n - 1;
        int scol = 0, ecol = n - 1;

        int num = 1;

        while (srow <= erow && scol <= ecol) {

            
            for (int j = scol; j <= ecol; j++) {
                matrix[srow][j] = num++;
            }
            srow++;

            
            for (int i = srow; i <= erow; i++) {
                matrix[i][ecol] = num++;
            }
            ecol--;

            
            if (srow <= erow) {
                for (int j = ecol; j >= scol; j--) {
                    matrix[erow][j] = num++;
                }
                erow--;
            }

            
            if (scol <= ecol) {
                for (int i = erow; i >= srow; i--) {
                    matrix[i][scol] = num++;
                }
                scol++;
            }
        }

        return matrix;
    }
}