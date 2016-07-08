import java.util.*;

public class LRUCache{
    public static void main(String[] args){
        LRUCache test = new LRUCache(3);
        System.out.println(test.get(1));
        printLRU(test);
        test.set(123,1);
        test.set(321,2);
        test.set(789,5);
        printLRU(test);
        System.out.println(test.get(123));
        test.set(777,6);
        printLRU(test);
    }

    public static void printLRU(LRUCache l){
        if(l.hm.size() > 0){
            System.out.println("start of hashmap");
            for(Integer name: l.hm.keySet()){
                String key = name.toString();
                System.out.println(key);
            }
            System.out.println("end of hashmap");
        }else{
            System.out.println("hash map is empty");
        }
    }

    private class Node{
        private int key;
        private int value;
        private Node prev;
        private Node next;

        public Node(int key, int value){
            this.key = key;
            this.value = value;
            prev = null;
            next = null;
        }
    }

    private int capacity;
    private HashMap<Integer, Node> hm = new HashMap<Integer, Node>();

    private Node head = new Node(-1, -1);
    private Node tail = new Node(-1, -1);


    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    // @return an integer
    public int get(int key) {
        if(!hm.containsKey(key)){
            return -1;
        }

        Node cur = hm.get(key);
        cur.prev.next = cur.next;
        cur.next.prev = cur.prev;

        move_to_tail(cur);
        return cur.value;
    }

    // @param key, an integer
    // @param value, an integer
    // @return nothing
    public void set(int key, int value) {
        if(get(key) != -1){
            hm.get(key).value = value;
            return;
        }

        if(hm.size() == capacity){
            hm.remove(head.next.key);
            head.next = head.next.next;
            head.next.prev = head;
        }

        Node insert = new Node(key, value);
        hm.put(key, insert);
        move_to_tail(insert);
    }

    private void move_to_tail(Node n){
        n.prev = tail.prev;
        n.next = tail;
        n.prev.next  = n;
        tail.prev = n;
    }
}

