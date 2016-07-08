public class strStr{
    public static void main(String[] args){
        String test = "abcdabcdefg";
        String test1 = "bcd";
        System.out.println(strStr(test, test1));
    }

    public static int strStr(String source, String target) {
        if(source == null || source == ""){
            return -1;
        }

        if(target == null || target == ""){
            return 0;
        }

        if(source.length() < target.length()){
            return -1;
        }

        int tLen = target.length();
        int sLen = source.length();
        for(int i = 0 ; i < (sLen - tLen + 1) ; i++){
            int j = 0;
            for(j = 0; j < tLen; j++){
                if(source.charAt(i + j) != target.charAt(j)){
                    break;
                }
            }

            if(j == tLen){
                return i;
            }
        }
        return -1;
    }
}
