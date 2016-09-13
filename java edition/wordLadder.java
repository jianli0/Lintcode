import java.util.*;

public class wordLadder{
    public static void main(String[] args){
        String start = "hit";
        String end = "cog";
        Set<String> dict = new HashSet<String>(){{
            add("hot"); add("dot");
            add("dog"); add("lot");
            add("log");
        }};
        int result = ladderLength(start, end, dict);
        System.out.println(result);
    }

    public static int ladderLength(String start, String end, Set<String> dict){
        if(dict == null){
            return 0;
        }
        if(start.equals(end)){
            return 1;
        }

        dict.add(start);
        dict.add(end);

        HashSet<String> hash = new HashSet<String>();
        Queue<String>  queue = new LinkedList<String>();
        queue.offer(start);
        hash.add(start);

        int length = 1;
        while(!queue.isEmpty()){
            length++;
            int size = queue.size();
            for(int i = 0; i < size; i++){
                String word = queue.poll();
                for(String nextWord: getNextWords(word, dict)){
                    if(hash.contains(nextWord)){
                        continue;
                    }
                    if(nextWord.equals(end)){
                        return length;
                    }
                    hash.add(nextWord);
                    queue.offer(nextWord);
                }
            }
        }
        return 0;
    }

    private static ArrayList<String> getNextWords(String word, Set<String> dict){
        ArrayList<String> nextWords = new ArrayList<String>();
        for(int i = 0; i < word.length(); i++){
            for(char c = 'a'; c <= 'z'; c++){
                if(c == word.charAt(i)){
                    continue;
                }
                String nextWord = replace(word, i, c);
                if(dict.contains(nextWord)){
                    nextWords.add(nextWord);
                }
            }
        }
        return nextWords;
    }

    private static String replace(String s, int index, char c){
        char[] chars = s.toCharArray();
        chars[index] = c;
        return new String(chars);
    }
}
