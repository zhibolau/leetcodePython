// 028 Max Revenue From Stock

// we are given an array of integers, stock. represents the prices.
// and we are given another array called algo, represents for the actions we need to take everyday. and in this array, we have 0 and 1 in this array originally, 0 means buy and 1 means sell.
// now we are also given a number, k, means we need to set a consecutive k elements to 1 that maximize the profit for the new actions. we can imagine the action of algo as robot, and it’s our job it modify them based on the k we are given to get as much profit as possible.

// return the maximum profit we can get.

public int maxRevenueFromStocks(int[] prices, int[] algo, int k) {
  if (prices == null || prices.length == 0) {
    return 0;
  }

  int runSum = 0;
  int n = algo.length;
  int i = 0;
  while (i < n) {
    if (algo[i] == 0) { //buy
      runSum -= prices[i];
    } else if (algo[i] == 1) { //sell
      runSum += prices[i];
    }
    i++;
  }

  int max = runSum;
  int j = k;
  while (j < n) {
    if (algo[j] == 0) runSum += 2 * prices[j];
    if (algo[j-k] == 0) runSum -= 2 * prices[j-k];
    max = Math.max(max, runSum);
    j++;
  }
  return max;
  
  
}
