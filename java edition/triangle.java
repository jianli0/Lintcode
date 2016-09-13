// bottom up

/*
public class classname{
    public static void main(String[] args){
        System.out.println();
    }

    public static (){

    }
}
*/

//top down
public class triangle{
    public static void main(String[] args){
        int[][] test = new int[][]{
            {2},
            {3, 4},
            {6, 5, 7},
            {4, 1, 8, 3}
        };

        int[][] test1 = new int[][]{
            {-1},
            {2, 3},
            {1, -1, -3}
        };

        System.out.println(minimumTotal(test));
    }

    public static int minimumTotal(int[][] triangle){
        if(triangle == null || triangle.length == 0){
            return 0;
        }
        int row = triangle.length;

        // define state
        int[][] f = new int[row][row];

        // initial
        f[0][0] = triangle[0][0];
        for(int i = 1; i < row; i++){
            f[i][0] = f[i - 1][0] + triangle[i][0];
            f[i][i] = f[i - 1][triangle[i-1].length - 1] + triangle[i][i];
        }

        //function
        for(int i = 1; i < row; i++){
            for(int j = 1; j < i; j++){
                f[i][j] = triangle[i][j] + Math.min(f[i - 1][j - 1], f[i - 1][j]);
            }
        }

        //answer
        int minRes = Integer.MAX_VALUE;
        for(int i = 0; i < f[row - 1].length; i++){
            // System.out.println(f[row - 1][i]);
            minRes = Math.min(minRes, f[row - 1][i]);
        }
        return minRes;
    }
}
