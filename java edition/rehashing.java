public class rehashing {
    public static void main(String[] args){
        ListNode a = new ListNode(21);
        ListNode b = new ListNode(9);
        ListNode c = new ListNode(14);

        ListNode[] test = new ListNode[4];
        test[1] = a;
        a.next = b;
        test[2] = c;

        ListNode[] testResult = rehashing(test);
        for(int i= 0 ; i < testResult.length; i++){
            System.out.println("index is " + i);
            printListNode(testResult[i]);
        }
    }

    public static ListNode[] rehashing(ListNode[] hashTable){
        if(hashTable.length <= 0){
            return hashTable;
        }

        int oldCap = hashTable.length;
        int newCap = 2 * oldCap;
        ListNode[] newHashTable = new ListNode[newCap];

        for(int i = 0; i < oldCap; i++){
            ListNode head = hashTable[i];
            while(head != null){
                int new_index = newIndex(head.val, newCap);
                if (newHashTable[new_index] == null){
                    newHashTable[new_index] = new ListNode(head.val);
                }else{
                    ListNode newHead = newHashTable[new_index];
                    while(newHead.next != null){
                        newHead = newHead.next;
                    }
                    newHead.next = new ListNode(head.val);
                }
                head = head.next;
            }
        }
        return newHashTable;
    }

    private static int newIndex(int val, int cap){
        if(val < 0){
            return (val % cap + cap) % cap;
        }
        return val % cap;
    }

    public static void printListNode(ListNode head){
        while(head!= null){
            System.out.println(head.val);
            head = head.next;
        }
    }
}
