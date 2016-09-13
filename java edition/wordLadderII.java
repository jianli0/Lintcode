import java.util.*;

public class Solution{
    public static void main(String args[]){
        String start = "hit";
        String end = "cog";
        Set<String> dict = new HashSet<String>(){{
            add("hot"); add("dot");
            add("dog"); add("lot");
            add("log");
        }};

        List<List<String>> result = findLadders(start, end, dict);
        for(List<String> i: result){
            System.out.println(i);
        }
    }

    public List<List<String>> findLadders(String start, String end, Set<String> dict){
        List<List<String>> ladders = new ArrayList<List<String>>();
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        Map<String, Integer> distance = new Map<String, Integer>();

        dict.add(start);
        dict.add(end);
        bfs(map, distance, start, end, dict);
        List<String> path = new ArrayList<String>();
        dfs(ladders, path, end, start, distance, map);

        return ladders;
    }

    private void bfs(Map<String, List<String>> map, Map<String,Integer> distance, String start,
            String end, Set<String> dict){
        Queue<String> q = new LinkedList<String>();
        q.offer(start);
        distance.put(start, 0);
        for(String s : dict){
            map.put(s, new ArrayList<String>());
        }

        while(!q.isEmpty()){
            String crt = q.poll();

            List<String> nextList = expand(crt, dict);
            for(String next: nextList){
                map.get(next).add(crt);
                if(!distance.containsKey(next)){
                    distance.put(next, distance.get(crt) + 1);
                    q.offer(next);
                }
            }
        }
    }

    private List<String> expand(String crt, Set<String> dict){
        List<String> expansion = new ArrayList<String>();

        for(int i = 0; i < crt.length(); i++){
            for(char ch = 'a'; ch <= 'z'; ch++){
                if(ch != crt.charAt(i)){
                    String expanded = crt.substring(0, i) + ch + crt.substring(i + 1);
                    if(dict.contains(expanded)){
                        expansion.add(expanded);
                    }
                }
            }
        }
        return expansion;
    }
}
