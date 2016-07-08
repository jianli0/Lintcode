import java.util.*;

public class largestRectangleArea{
    public static void main(String[] args){
        int[] test = new int[]{2, 1, 5, 6, 2, 3};
        System.out.println(largestRectangleArea(test));
    }

    public static int largestRectangleArea(int[] height){
        if(height == null || height.length == 0){
            return 0;
        }

        Stack<Integer> stack = new Stack<Integer>();

        int maxArea = 0;

        for(int i = 0 ; i <= height.length; i++){
            int curt = (i == height.length)? -1 : height[i];
            while(!stack.isEmpty() && curt <= height[stack.peek()] ){
                int h = height[stack.pop()];
                int w = stack.isEmpty()? i : (i - stack.peek() - 1);
                maxArea = Math.max(maxArea, h * w);
            }
            stack.push(i);
        }
        return maxArea;
    }
}
