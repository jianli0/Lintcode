import java.util.*;
public class cloneGraph{
    public static void main(String[] args){
        System.out.println();
    }

    public static UndirectedGraphNode cloneGraph(UndirectedGraphNode node){
        if(node == null){
            return node;
        }

        // 1. use bfs algorithm to traverse the graph and get all nodes
        ArrayList<UndirectedGraphNode> nodes = getNodes(node);

        // 2. cope nodes, store the old -> new mapping in a hash map
        HashMap<UndirectedGraphNode, UndirectedGraphNode> hm = new HashMap<>();
        for(UndirectedGraphNode n : nodes){
            hm.put(n, new UndirectedGraphNode(n.label));
        }

        // 3. copy neighbors(edges)
        for(UndirectedGraphNode n : nodes){
            UndirectedGraphNode newNode = hm.get(n);
            for(UndirectedGraphNode nb : n.neighbors){
                UndirectedGraphNode newNb = hm.get(nb);
                newNode.neighbors.add(newNb);
            }
        }
        return hm.get(node);
    }

    private static ArrayList<UndirectedGraphNode> getNodes(UndirectedGraphNode node){
        Queue<UndirectedGraphNode> queue = new LinkedList<UndirectedGraphNode>();
        HashSet<UndirectedGraphNode> set = new HashSet<UndirectedGraphNode>();
        queue.offer(node);
        set.add(node);

        while(!queue.isEmpty()){
            UndirectedGraphNode head = queue.poll();
            for(UndirectedGraphNode i : head.neighbors){
                if(!set.contains(i)){
                    queue.offer(i);
                    set.add(i);
                }
            }
        }
        return new ArrayList<UndirectedGraphNode>(set);
    }
}
