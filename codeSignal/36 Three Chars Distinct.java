// 036 Three Chars Distinct
// given a string s, find out all the substring of this string with length equals to 3 that all of its three chars are distinct.
// get the number of substring that meets the requirements. return the value.

// this problem is pretty straight forward too.
// but I’m thinking there might be better solutions than this brute force.

public int threeCharsDistinct(String s) {
  if (s == null || s.length() < 3) return 0;

  int i = 0;
  int res = 0;
  while (i <= s.length() - 3) {
    if (checkDistinct(s.substring(i, i + 3)) != 0) { //equals 0 means we have duplicates
      res++;
    }
    i++;
  }
  return res;
  
}

private int checkDistinct(String s) { //the length of it must be 3
  int res = s.charAt(0);
  int i = 1;
  while (i < s.length()) {
    res = s.charAt(i)^res;
    i++;
  }
  return res;
}
