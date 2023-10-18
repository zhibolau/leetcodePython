import java.util.List;
import java.util.Objects;

public class LinkedLiistShoppingCart {
    public static void main(String[] args) {

    }
    static class ListNode {
        String val;
        ListNode next;
        ListNode() {}
        ListNode(String val) { this.val = val; }
        ListNode(String val, ListNode next) { this.val = val; this.next = next; }
    }
    public ListNode getShoppingCart(ListNode head, List<List<String>> operations) {
        ListNode dummy = new ListNode(null, head);
        ListNode tail = dummy.next;
        while (tail.next != null) {
            tail = tail.next;
        }
        for (List<String> operation : operations) {
            if (dummy.next == null) {
                tail = dummy;
            }
            switch (operation.get(0)) {
                case "PUSH_HEAD":
                    dummy.next = new ListNode(operation.get(1), dummy.next);
                    break;
                case "PUSH_TAIL":
                    ListNode node = new ListNode(operation.get(1), null);
                    tail.next = node;
                    tail = node;
                    break;
                case "POP_HEAD":
                    if (dummy.next != null) {
                        dummy.next = dummy.next.next;
                    }
                    break;
            }
        }
        return dummy.next;
    }
}

