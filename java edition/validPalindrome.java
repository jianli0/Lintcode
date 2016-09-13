public class validPalindrome{
    public static void main(String[] args){
        String test = "a.";
        System.out.println(isPalindrome(test));
    }

    public static boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;
        while(start < end){
            while(!isValidChar(s.charAt(start))){
                start++;
            }
            while(!isValidChar(s.charAt(end))){
                end--;
            }
            System.out.println(start + "\t" + end);
            if(start < end){
                if(s.charAt(start) != s.charAt(end)){
                    return false;
                }
            }
        }
        return true;
    }

    private static boolean isValidChar(char c){
        if(c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z'){
            return true;
        }
        return false;
    }
}
