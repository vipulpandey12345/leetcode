class Solution {
    ArrayList<Integer> list = new ArrayList<>();
    public TreeNode sortedListToBST(ListNode head) {
        populateList(head);
        return recursive(list);
    }


    public void populateList(ListNode head) {
        ListNode headCopy = head;
        while (headCopy != null) {
            list.add(headCopy.val);
            headCopy = headCopy.next;
        }
    }

    public TreeNode recursive(List<Integer> list) {
        TreeNode curr = new TreeNode();
        if (list.size() == 0) {
            return null;
        } 
        if (list.size() == 1) {
            curr.val = list.get(0);
            return curr;
        }
        int half = list.size() / 2;
        int currVal = list.get(half);
        curr.val = currVal;
        curr.left = recursive(list.subList(0, half));
        curr.right = recursive(list.subList(half + 1, list.size()));
        return curr;
    }
}
