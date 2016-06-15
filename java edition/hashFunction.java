public class hashFunction{
    public static void main(String[] args){
        char[] test = new char[]{'u','b','u','n','t','u'};
        System.out.println(hashCode(test, 1007));
    }

    public static int hashCode(char[] key,int HASH_SIZE) {
        if(key == null || key.length == 0 || HASH_SIZE == 0){
            return 0;
        }
        long res = 0;

        for(int i = 0; i < key.length; i++){
            res += (int)key[i] * Math.pow(33,(key.length - i - 1));
            System.out.println((int)key[i] + "\t" + (key.length - i - 1));
            System.out.println(res);
        }
        return res % HASH_SIZE;
    }
}
