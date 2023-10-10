// ; 037 Boolean Deque
// ; given an integer n, represents the length of a binary string a, initialized with 0s

// ; and we are also given an array called operations, it contains strings of one of the following two:
// ; “L” - find the first 0 starting form the left, reassign it with 1
// ; C{index} - set a.charAt(index)=0

// ; the return value should be the binary string after all the operations have been applied.

//use bit operation to make ajustment on string
public String booleanDequeBit(int n, String[] oper) {
  if (n == 0) {
    return new String();
  }

  int res = 0;
  for (int i = 0; i < oper.length; i++) {
    if (oper[i].equals("L")) {
      int k = n;
      while (k > 0) {
        int cur = (res >> (k - 1) & 1);
        if (cur == 1) {
          k--;
        } else {
          res = res | ((k - 1) << 1);
          break;
        }
      }
    } else { //find index = i and set the value to 0
      int digit = oper[i].charAt(1) - '0';
      res = res & (~(n - digit - 1))
    }
  }
  return Integer.toBinaryString(res);
}
