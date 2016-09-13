import java.util.*;

public class palindromePartition{
    public static void main(String[] args){
        String test = "aab";
        List<
        System.out.println();
    }

    public ArrayList<ArrayList<String>> partition(String s) {
        ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
        if(s == null){
            return result;
        }
        ArrayList<String> path = new ArrayList<String>();
        helper(s, path, 0, result);

        return result;
    }

    private void helper(String s, ArrayList<String> path, int pos, ArrayList<ArrayList<String>> result){
        if(pos == s.length()){
            result.add(new ArrayList<String>(path));
            return;
        }

        for(int i = pos + 1; i <= s.length(); i++){
            String prefix = s.substring(pos, i);
            if(!ifPalindrome(prefix)){
                continue;
            }
            path.add(prefix);
            helper(s, path, i, result);
            path.remove(path.size() - 1);
        }
    }

    private boolean isPalindrome(String s){
        int start = 0;
        int end = s.length() - 1;
        while(start < end){
            if(s.charAt(start) != s.charAt(end)){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }

}
