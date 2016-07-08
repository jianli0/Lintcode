import java.util.*;
public class nQueens{
    public static void main(String[] args){
        int test = 4;
        ArrayList<ArrayList<String>> result = solveNQueens(test);

        for(int i = 0; i < result.size(); i++){
            System.out.println(result.get(i));
        }
    }

    public static ArrayList<ArrayList<String>> solveNQueens(int n){
        ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
        if(n <= 0){
            return result;
        }
        ArrayList<Integer> cols = new ArrayList<Integer>();
        search(n, cols, result);

        return result;
    }

    private static void search(int n, ArrayList<Integer> cols, ArrayList<ArrayList<String>> result){
        if(cols.size() == n){
            result.add(drawChessboard(cols));
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

    private static ArrayList<String> drawChessboard(ArrayList<Integer> cols){
        ArrayList<String> chessBoard = new ArrayList<String>();
        for(int i = 0; i < cols.size(); i++){
            String chessboardRow = "";
            for(int j = 0; j < cols.size(); j++){
                if(j == cols.get(i)){
                    chessboardRow += "Q";
                }else{
                    chessboardRow += ".";
                }
            }
            chessBoard.add(chessboardRow);
        }
        return chessBoard;
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

}
