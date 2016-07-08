import java.util.*;
class nQueensII{
    public static void main(String[] args){
        int test = 1;
        int result = totalNQueens(test);

        int test1 = 4;
        // int result1 = totalNQueens(test1);

        System.out.println(result);
    }

    public static int totalNQueens(int n){
        int result = 0;
        if(n <= 0){
            return result;
        }
        ArrayList<Integer> cols = new ArrayList<Integer>();
        search(n, cols, result);

        return result;
    }

    private static void search(int n, ArrayList<Integer> cols, int result){
        System.out.println(cols);
        if(cols.size() == n){
            result += 1;
            return;
        }

        for(int col = 0; col < n; col++){
            if(!isValid(cols, col)){
                continue;
            }
            cols.add(col);
            search(n, cols, result);
            cols.remove(cols.size() - 1);
        }
    }

    private static boolean isValid(ArrayList<Integer> cols, int col){
        int row = cols.size();
        for(int i = 0; i < row; i++){
            if(cols.get(i) == col){
                return false;
            }

            // left top to right bottom
            if(i - cols.get(i) == row - col){
                return false;
            }

            // right top to left bottom
            if(i + cols.get(i) == row + col){
                return false;
            }
        }
        return true;
    }
};


