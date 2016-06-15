import java.util.*;
public class intersectionOfTwoArrays{
    public static void main(String[] args){
        int[] test1 = new int[]{1,2,2,1};
        int[] test2 = new int[]{2,2};
        System.out.println(intersection(test1,test2));
    }

    public static int[] intersection(int[] nums1, int[] nums2) {
        if(nums1 == null || nums1.length == 0 || nums2 == null || nums2.length == 0){
            return null;
        }

        int count = Math.max(nums1.length, nums2.length);
        HashSet<Integer> rst = new HashSet<Integer>();
        HashSet<Integer> n1 = new HashSet<Integer>();

        for(Integer i: nums1){
            n1.add(i);
        }

        for(Integer j : nums2){
            if(n1.contains(j)){
                rst.add(j);
            }
        }
        System.out.println("hello world");
        System.out.println(rst);

        int[] result = new int[rst.size()];
        result = rst.toArray(result);
    }
}
