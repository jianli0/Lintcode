public class uniquePathsII{
    public static void main(String[] args){
        int[][] test = new int[][]{
            {0, 0, 0},
            {0, 1, 0},
            {0, 0, 0}
        };

        int[][] test1 = new int[][]{
            {0, 0},
            {0, 0},
            {0, 0},
            {1, 0},
            {0, 0}
        };

        System.out.println(uniquePathsWithObstacles(test1));
    }

    public static int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid == null || obstacleGrid.length == 0){
            return 0;
        }

        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        int[][] f = new int[m][n];
        if(obstacleGrid[0][0] == 1){
            return 0;
        }else{
            f[0][0] = 1;
        }

        for(int i = 1; i < m ; i++){
            if(obstacleGrid[i][0] == 1){
                for(int k = i; k < m; k++){
                    f[i][0] = 0;
                }
                break;
            }else{
                f[i][0] = 1;
            }
        }

        for(int j = 1; j < n ; j++){
            if(obstacleGrid[0][j] == 1){
                for(int k = j; k < n; k++){
                    f[0][j] = 0;
                }
                break;
            }else{
                f[0][j] = 1;
            }
        }

        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                f[i][j] = obstacleGrid[i][j] == 1 ? 0 : (f[i - 1][j] + f[i][j - 1]);
            }
        }
        return f[m - 1][n - 1];
    }
}

