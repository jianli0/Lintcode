import java.util.*;

public class rotateString{
    public static void main(String[] args){
        char[] str = new char[]{'a', 'b', 'c', 'd', 'e', 'f', 'g'};
        rotateString(str, 3);

    }

    public static void rotateString(char[] str, int offset) {
        if(str == null || str.length == 0 || offset == 0){
            return;
        }
        offset = offset % str.length;
        reverse(str, 0, offset);
        reverse(str, offset + 1, str.length - 1);
        reverse(str, 0, str.length - 1);
    }

    private static void reverse(char[] str, int start, int end){
        while(start < end){
            System.out.println(start + "\t" + end);
            char tmp = str[start];
            str[start] = str[end];
            str[end] = tmp;
            start += 1;
            end -= 1;
        }
    }
}
