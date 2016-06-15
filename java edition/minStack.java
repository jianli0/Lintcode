import java.util.*;

public class minStack{
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
        private Stack<Integer> stack = new Stack<Integer>();
        private Stack<Integer> minStack = new Stack<Integer>();
    }

    public void push(int number) {
        stack.push(number);
        if(minStack.empty() == true || number <= minStack.peek()){
            minStack.push(number);
        }
    }

    public int pop() {
        if(stack.peek() == minStack.peek()){
            minStack.pop();
        }
        return stack.pop();
        // write your code here
    }

    public int min() {
        return minStack.peek();
    }

}
