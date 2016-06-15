import java.util.*;
public class productOfArrayExcludeItself{
    public static void main(String[] args){
        ArrayList<Integer> test = new ArrayList<Integer>();
        test.add(1);
        test.add(2);
        test.add(3);
        test.add(4);
        test.add(5);
        System.out.println(productExcludeItself(test));
    }

    public static ArrayList<Long> productExcludeItself(ArrayList<Integer> A) {
        ArrayList<Long> product = new ArrayList<Long>();
        if (A == null){
            return product;
        }

        int count = A.size();

        if (count == 1){
            product.add(Long.valueOf(1));
            return product;
        }


        long[] left = new long[count];
        long[] right = new long[count];

        left[0] = 1;
        right[0] = 1;

        for(int i = 1; i < count; i++){
            left[i] = A.get(i-1) * left[i - 1];
            right[i] = A.get(count - i) * right[i - 1];
        }

        for(int k = 0; k < count; k++){
            product.add(Long.valueOf(left[k] * right[count - 1 - k]));
        }

        System.out.println(Arrays.toString(left));
        System.out.println(Arrays.toString(right));
        return product;
        // write your code
    }
}
