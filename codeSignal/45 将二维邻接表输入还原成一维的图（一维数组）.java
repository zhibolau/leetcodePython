# 045 将二维邻接表输入还原成一维的图（一维数组）


# for example:
# input: [[6, 5], [2, 3], [4, 3], [4, 5], [1, 2]]
# output: [1, 2, 3, 4, 5, 6] or [6,5,4,3,2,1]

# 类似拓扑排序，用一个map保存每个点和他的邻接列表，那么 入度为0的点要么是一维数组的头要么是尾。从这个点开始，遍历map或者遍历二维数组 就完事了


public int[] adjArrayto1dArray(int[][] edges) {
  HashMap<Integer, Integer> map = new HashMap<>();
  for (int[] edge: edges) {
    ...
  }
}
