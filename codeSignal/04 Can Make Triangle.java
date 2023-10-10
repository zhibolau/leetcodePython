//004 Can Make Triangle

// given an array with all the elements are positive.
// check if elements can form a triangle.

// return an array called res, with length of arr.length-2, and res[i] = 1 if it is possible to form a triangle with arr[i] arr[i+1], arr[i+2], otherwise 0;

int len = arr.length;
int[] res = new int[len - 2];
for (int i = 0; i <= len - 3; i++) {
  if (check(arr[i], arr[i+1], arr[i+2])) {
    res[i] = 1;
  } else res[i] = 0;
}
return res;

private boolean check(int i, int j, int k) {
  return (i+j>k && i+k>j && j+k>i && Math.abs(i-j)<k && Math.abs(i-k)<j && Math.abs(j-k)<i);
}
