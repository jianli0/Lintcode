import java.util.*;

public class fourSum{
    public static void main(String[] args){
        int[] test = new int[]{1, 0 , -1, 0, -2 ,2};
        int target = 0;
        ArrayList<ArrayList<Integer>> result = fourSum(test, target);
        for(ArrayList<Integer> i : result){
            for(Integer j : i){
                System.out.println(j);
            }
            System.out.println("end of one solution");
        }
    }

    public static ArrayList<ArrayList<Integer>> fourSum(int[] numbers, int target){
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if(numbers == null || numbers.length == 0){
            return result;
        }

        Arrays.sort(numbers);

        for(int i = 0; i < numbers.length - 3; i++){
            if(i != 0 && numbers[i] == numbers[i - 1]){
                continue;
            }
            for(int j = i + 1; j < numbers.length - 2; j++){
                if(j != i + 1 && numbers[j] == numbers[j - 1]){
                    continue;
                }
                int firstTwoSum = numbers[i] + numbers[j];
                int left = j + 1;
                int right = numbers.length - 1;
                while(left < right){
                    if(left != j + 1 && numbers[left] == numbers[left - 1]){
                        left++;
                    }
                    if(right != numbers.length - 1 && numbers[right] == numbers[right + 1]){
                        right--;
                    }
                    if(left < right){
                        if(numbers[left] + numbers[right] + firstTwoSum < target){
                            left++;
                        }else if(numbers[left] + numbers[right] + firstTwoSum > target){
                            right--;
                        }else{
                            ArrayList<Integer> cur = new ArrayList<Integer>();
                            cur.add(numbers[i]);
                            cur.add(numbers[j]);
                            cur.add(numbers[left]);
                            cur.add(numbers[right]);
                            result.add(cur);
                            left++;
                            right--;
                        }
                    }
                }
            }
        }
        return result;
    }
}
