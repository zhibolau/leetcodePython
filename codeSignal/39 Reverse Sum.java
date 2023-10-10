039 Reverse Sum

public int reverseSum(int[] numbers) {
  int res = 0;
  for (int number: numbers) {
    char[] num = number.toCharArray();
    int i = 0;
    int j = num.length - 1;
    while (number[j] == '0') {
      j--;
    }
    while (i <= j) {
      //swap the char of index i and j
      i++;
      j++;
    }
    res += (int)String.valueOf(number);
  }
  return res;
}
