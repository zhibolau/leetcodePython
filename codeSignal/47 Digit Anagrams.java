// 047 Digit Anagrams
// Given an array of integers, a, count the number of pairs of i and j such that a[i] and a[j] are digit anagrams.

// idea: for each integer, make it to charArray and sort it, and store them in hashmap, for every key that its corresponding value larger than 1(means have anagrams), the pair for this key is (v*(v-1))/2


public int digitAnagrams(int[] nums) {
  if (nums == null || nums.length < 2) {
    return 0;
  }
  int res = 0;
  HashMap<String, Integer> map = new HashMap<>();
  for (int num: nums) {
    char[] temp = String.valueOf(num).toCharArray();
    Arrays.sort(temp);
    String key = String.valueOf(temp);
    map.put(key, map.getOrDefault(key, 0) + 1);
  }
  for (Integer v: map.values()) {
    if (v != 1) {
      res += v * (v - 1) / 2;
    }
  }
  return res;
}
