
//brute force but fails if no 0 are present and -1 is already present
class SetMatrixZero {

    public static void setrow(int[][] matrix, int r, int c) {
        for (int i = 0; i < c; i++) {
            if (matrix[r][i] != 0) {
                matrix[r][i] = -1;
            }
        }
    }

    public static void setcolumn(int[][] matrix, int r, int c) {
        for (int j = 0; j < r; j++) {
            if (matrix[j][c] != 0) {
                matrix[j][c] = -1;
            }
        }
    }

    public static void setZeroes(int[][] matrix) {
        int r = matrix.length;
        int c = matrix[0].length;
        System.out.println(r + " " + c);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (matrix[i][j] == 0) {
                    setrow(matrix, i, c);
                    setcolumn(matrix, r, j);
                }
            }
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (matrix[i][j] == -1) {
                    matrix[i][j] = 0;
                }
            }
        }
        // print matrix
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}

//better
class Solution{
    public static void setZeroes(int[][] matrix) {
        int r = matrix.length;
        int c = matrix[0].length;
        int[] trackrow = new int[r];
        int[] trackcolumn = new int[c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (matrix[i][j] == 0) {
                    trackrow[i] = 1;
                    trackcolumn[j] = 1;
                }
            }
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (trackrow[i] == 1 || trackcolumn[j] == 1) {
                    matrix[i][j] = 0;
                }
            }
        }
        // print matrix

    }
}
public class A17_set_matrix {
    public static void main(String args[]) {
        int[][] matrix = {
                { 1, 2, 3, 4 },
                { 5, 0, 7, 8 },
                { 9, 10, 11, 0 }
        };
        //brute force
        SetMatrixZero.setZeroes(matrix);
        //better
        Solution.setZeroes(matrix);

    }
}
