import java.util.*;

class subSetII{
    public static void main(String[] args){
        ArrayList<Integer> test = new ArrayList<Integer>();
        test.add(1);
        test.add(2);
        test.add(3);

        ArrayList<ArrayList<Integer>> result = subsetsWithDup(test);
        for(int i = 0; i < result.size(); i++){
            System.out.println("final result is " + result.get(i));
        }
    }

    public static ArrayList<ArrayList<Integer>> subsetsWithDup(ArrayList<Integer> S) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if(S == null || S.size() == 0){
            return result;
        }

        Collections.sort(S);
        ArrayList<Integer> temp = new ArrayList<Integer>();
        helper(result, temp, S ,0);

        return result;
    }

    private static void helper(ArrayList<ArrayList<Integer>> result, ArrayList<Integer> temp,
            ArrayList<Integer> S, int pos){
        result.add(new ArrayList<Integer>(temp));

        for(int i = pos; i < S.size() ; i++){
            temp.add(S.get(i));
            helper(result, temp, S, i + 1);
            temp.remove(temp.size() - 1);
        }
    }
}
