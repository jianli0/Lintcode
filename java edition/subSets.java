import java.util.*;

public class subSets{

    public static void main(String[] args){
        int[] test = new int[]{1, 2, 3};
        ArrayList<ArrayList<Integer>> res = subsets(test);
        for(ArrayList<Integer> i : res){
            System.out.println(i);
        }
    }

    public static ArrayList<ArrayList<Integer>> subsets(int[] num){
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if(num == null || num.length == 0){
            return result;
        }

        ArrayList<Integer> cur = new ArrayList<Integer>();
        Arrays.sort(num);
        subsetsHelper(result, cur, num, 0);
        return result;
    }

    private static void subsetsHelper(ArrayList<ArrayList<Integer>> result,
        ArrayList<Integer> cur, int[] num, int pos){
        result.add(new ArrayList<Integer>(cur));

        for(int i = pos; i < num.length; i++){
            cur.add(num[i]);
            subsetsHelper(result, cur, num, i + 1);
            cur.remove(cur.size() - 1);
        }
    }
}
