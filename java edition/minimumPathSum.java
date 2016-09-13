public class minimumPathSum{
    public static void main(String[] args){
        int[][] test = new int[][]{
            {1, 2, 3},
            {6, 5, 4},
            {7, 9, 8}
        };
        System.out.println(minPathSum(test));
    }

    public static int minPathSum(int[][] grid){
        if(grid == null || grid.length == 0){
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;

        // state
        int[][] f = new int[m][n];

        f[0][0] = grid[0][0];
        // initial
        for(int i = 1; i < m; i++){
            f[i][0] = f[i - 1][0] + grid[i][0];
        }

        for(int j = 1; j < n; j++){
            f[0][j] = f[0][j - 1] + grid[0][j];
        }

        // function
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                f[i][j] = Math.min(f[i - 1][j], f[i][j - 1]) + grid[i][j];
                // System.out.println(f[i][j]);
            }
        }
        return f[m - 1][n - 1];
    }
}

