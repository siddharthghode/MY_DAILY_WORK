class Solution {
    public static void rotate_matrix(int[][] matrix) {
        int n = matrix.length;
        // transpose
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        // reverse the rows
        for (int i = 0; i < n; i++) {
            int left = 0;
            int right = n - 1;

            while (left < right) {
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;

                left++;
                right--;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println(" ");
        }
    }
}

public class A18_rotate_matrix {
    public static void main(String args[]) {
        int[][] matrix = {
                { 1, 2, 3 },
                { 5, 0, 7 },
                { 9, 10, 11 }
        };
        Solution.rotate_matrix(matrix);
    }
}
