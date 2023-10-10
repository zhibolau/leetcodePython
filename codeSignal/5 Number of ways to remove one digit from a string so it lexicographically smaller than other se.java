005 Number of ways to remove one digit from a string so it lexicographically smaller than other se

Given two string, s and t.
both consisting of lowercase letters and digits.
now we want to make s lexicographically smaller than t.
rules: remove only one digit from s.
now return how many ways can we do this.

Pay attention: digits are smaller than letter in lexicographically way.



public int removeOneDigit(String s, String t) {
  int sLen = s.length();
  int tLen = t.length();

  int count = 0;
  check(s, sLen, count, t);
  check(t, tLen, count, s);
  return count;
  // for (int i = 0; i < sLen; i++) {
  //   if (Character.isDigit(s.charAt(i))) {
  //     String temp = s.substring(0, i) + s.substring(i+1);
  //     if (temp.compareTo(t) < 0) {
  //       count++;
  //     }
  //   }
  // }
  // //and then we try it on t 
  // for (int i = 0; i < tLen; i++) {
  //   if (Character.isDigit(t.charAt(i))) {
  //     String temp = t.substring(0, i) + t.substring(i+1);
  //     if (temp.compareTo(s) < 0) {
  //       count++;
  //     }
  //   }
  // }
  // return count;
}
private void check(String s, int len, int count, String t) {
  for (int i = 0; i < len; i++) {
    if (Character.isDigit(s.charAt(i))) {
      String temp = s.substring(0, i) + s.substring(i+1);
      if (temp.compareTo(t) < 0) {
        count++;
      }
    }
  }
}
