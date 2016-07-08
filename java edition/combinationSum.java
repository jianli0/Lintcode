import java.util.*;

public class combinationSum{
    public static void main(String[] args){
        int[] test = new int[]{2, 2, 3, 6, 7};
        int target = 7;
        ArrayList<ArrayList<Integer>> result = combinationSum(test, target);

        for(ArrayList<Integer> i : result){
            System.out.println(i);
        }
    }

    public static ArrayList<ArrayList<Integer>> combinationSum(int[] candidates, int target){
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if(candidates == null || candidates.length == 0){
            return result;
        }

        ArrayList<Integer> path = new ArrayList<Integer>();
        Arrays.sort(candidates);
        helper(candidates, target, path, 0, result);

        return result;
    }

    private static void helper(int[] candidates, int target, ArrayList<Integer> path, int index,
            ArrayList<ArrayList<Integer>> result){
        if(target == 0){
            result.add(new ArrayList<Integer>(path));
            return;
        }

        int prev = -1;
        for(int i = index; i < candidates.length; i++){
            if(candidates[i] > target){
                break;
            }

            if(prev != -1 && prev == candidates[i]){
                continue;
            }
            path.add(candidates[i]);
            helper(candidates, target - candidates[i], path, i, result);
            path.remove(path.size() - 1);

            prev = candidates[i];
        }
    }
}
