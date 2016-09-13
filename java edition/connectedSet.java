import java.util.*;

public class connectedSet{
    public static void main(String[] args){
        UndirectedGraphNode a1 = new UndirectedGraphNode(1);
        UndirectedGraphNode a2 = new UndirectedGraphNode(2);
        UndirectedGraphNode a3 = new UndirectedGraphNode(3);
        UndirectedGraphNode a4 = new UndirectedGraphNode(4);
        UndirectedGraphNode a5 = new UndirectedGraphNode(5);
        UndirectedGraphNode a6 = new UndirectedGraphNode(6);
        UndirectedGraphNode a7 = new UndirectedGraphNode(7);

        a1.neighbors.add(a2);

        a2.neighbors.add(a1);
        a2.neighbors.add(a3);
        a2.neighbors.add(a4);

        a3.neighbors.add(a2);
        a3.neighbors.add(a4);

        a4.neighbors.add(a2);
        a4.neighbors.add(a3);

        a5.neighbors.add(a6);
        a5.neighbors.add(a7);

        a6.neighbors.add(a5);
        a6.neighbors.add(a7);

        a7.neighbors.add(a5);
        a7.neighbors.add(a6);

        ArrayList<UndirectedGraphNode> test = new ArrayList<UndirectedGraphNode>();
        test.add(a1); test.add(a2);test.add(a3);test.add(a4);test.add(a5);test.add(a6);test.add(a7);
        List<List<Integer>> result = connectedSet(test);
        for(List<Integer> i : result){
            System.out.println(i);
        }
    }

    public static List<List<Integer>> connectedSet(ArrayList<UndirectedGraphNode> nodes){
        int m = nodes.size();
        HashMap<UndirectedGraphNode, Boolean> visited = new HashMap<UndirectedGraphNode, Boolean>();

        for(UndirectedGraphNode node: nodes){
            visited.put(node, false);
        }

        List<List<Integer>> result = new ArrayList<>();

        for(UndirectedGraphNode node : nodes){
            if(visited.get(node) == false){
                bfs(node, visited, result);
            }
        }
        return result;
    }

    public static void bfs(UndirectedGraphNode node, HashMap<UndirectedGraphNode, Boolean> visited,
            List<List<Integer>> result){
        List<Integer> row = new ArrayList<Integer>();
        Queue<UndirectedGraphNode> queue = new LinkedList<UndirectedGraphNode>();

        visited.put(node, true);
        queue.offer(node);

        while(!queue.isEmpty()){
            UndirectedGraphNode u = queue.poll();
            row.add(u.label);
            for(UndirectedGraphNode v: u.neighbors){
                if(visited.get(v) == false){
                    visited.put(v, true);
                    queue.offer(v);
                }
            }
        }
        Collections.sort(row);
        result.add(row);
    }
}
