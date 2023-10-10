就是对于每个b_i来说都去找离它最近的那个a_k，然后gain_i就是|b_i - a_i| - |b_i - a_k|，意为如果替换当前的b对应的a能达到的最大收益。
找到最大的gain，sum(diff)减去其即可。我用了二分去找离b_i最近的a_k，不清楚如果直接找会不会超时，不妨试试。

public int findminAbs(int[] a, int[] b) {
  int res = 0;
  //for every bi, we need to find the cloasest in a
  //so we need to use binary search for sorted array a, that closest in break;
  Arrays.sort(a);
  for (int num: b) {
    int ak = binarySearch(num, a);
    res += Math.abs(num - ak);
  }
  return res;
}
private int binarySearch(int num, int[] a) {
  if (num < a[0]) {
    return a[0];
  }
  if (num > a[a.length - 1]) {
    return a[a.length - 1];
  }
  int lo = 0;
  int hi = a.length - 1;
  while (lo <= hi) {
    int mid = (hi - lo) / 2 + lo;
    if (value < a[mid]) {
      hi = mid - 1;
    } else if (value > a[mid]) {
      lo = mid + 1;
    } else {
      return a[mid];
    }
    
  }
  //the final position of lo and hi will be lo == hi + 1
  return (a[lo] - value) < (value - a[hi]) ? a[lo] : a[hi];
}
