import java.util.*;
public class topSort{
    public static void main(String[] args){
        ArrayList<DirectedGraphNode> test = new ArrayList<DirectedGraphNode>();
        // nodes
        DirectedGraphNode a = new DirectedGraphNode(0);
        DirectedGraphNode b = new DirectedGraphNode(1);
        DirectedGraphNode c = new DirectedGraphNode(2);
        DirectedGraphNode d = new DirectedGraphNode(3);
        DirectedGraphNode e = new DirectedGraphNode(4);
        DirectedGraphNode f = new DirectedGraphNode(5);

        // edges
        a.neighbors.add(b);
        a.neighbors.add(c);
        a.neighbors.add(d);

        b.neighbors.add(e);

        c.neighbors.add(e);
        c.neighbors.add(f);

        d.neighbors.add(e);
        d.neighbors.add(f);

        test.add(a); test.add(b);
        test.add(c); test.add(b);
        test.add(e); test.add(f);

        ArrayList<DirectedGraphNode> testRes = topSort(test);
        for(DirectedGraphNode i : testRes){
            System.out.println(i.label);
        }
    }

    public static ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph){
        ArrayList<DirectedGraphNode> result = new ArrayList<DirectedGraphNode>();
        if(graph == null || graph.size() == 0){
            return result;
        }
        HashMap<DirectedGraphNode, Integer> hm = new HashMap<DirectedGraphNode, Integer>();
        for(DirectedGraphNode node : graph){
            for(DirectedGraphNode neighbor : node.neighbors){
                if(!hm.containsKey(neighbor)){
                    hm.put(neighbor, 1);
                }else{
                    hm.put(neighbor, hm.get(neighbor) + 1);
                }
            }
        }

        Queue<DirectedGraphNode> q = new LinkedList<DirectedGraphNode>();
        for(DirectedGraphNode node : graph){
            if(!hm.containsKey(node)){
                q.offer(node);
                result.add(node);
            }
        }

        while(!q.isEmpty()){
            DirectedGraphNode cur = q.poll();
            for(DirectedGraphNode neighbor : cur.neighbors){
                hm.put(neighbor, hm.get(neighbor) - 1);
                if(hm.get(neighbor) == 0){
                    q.offer(neighbor);
                    result.add(neighbor);
                }
            }
        }
        return result;
    }
}
