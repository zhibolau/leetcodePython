// 035 Divide SubString
// given a number n and a length k
// now we need to know that from all the substring of number n with length of k, how many of these can be divisible by n.
// return the number of substrings that meets the requirement.


public int divideSubstring(int n, int k) {
  if (n == 0 || k == n) return 0;

  String str = Integer.toString(n);
  int len = str.length();
  int count = 0;
  for (int i = 0; i <= len - k; i++) {
    String cur = str.substring(i, i + k);
    if (Integer.parseInt(cur) % k == 0) {
      count++;
    }
  }
  return count;
}

