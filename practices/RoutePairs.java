import java.util.*;

/**
 * divides shipping routes using flight optimization routing systems to a cluster of aircrafts that can fulfill these routes
 * each shipping route is identified by a unique integer identifier, requires a fixed non-0 amount of travel distance bwtween airports
 * and is defined to be either a forward shipping route or a return shipping route
 * identifiers are guaranteed to be unique whithin their own route type, but not across route types
 *
 * if aircraft has max operating travel dist = 3000 miles, a forward/return shipping route pair using 2900 would be optimal
 * but not optimal if there exists a pair that uses a total dist 3000 miles
 *
 * i.e. maxTravelDist = 7000, forwardRouteList=[1,2000][2,4000][3,6000]
 * returnRouteList=[1,2000]
 * output [2,1]
 * explain: 3 combinations:[1,1] [2,1] [3.1] -> total 4000, 6000, 8000 miles, 6000 is the optimal < 7000, so [2,1]
 *
 * i.e 2
 * maxdist = 10000, forward=[1,2000][2,5000][3,7000][4,10000]
 * returnList=[1,2000],[2,3000],[3,4000],[4,5000]
 * ans: [2,4][3,2]
 */
public class RoutePairs {

    public List<List<Integer>> routePairs(int maxTravelDist, List<List<Integer>> forwardRouteList, List<List<Integer>> returnRouteList) {
        forwardRouteList.sort(Comparator.comparingInt(i -> i.get(1)));
        returnRouteList.sort(Comparator.comparingInt(i -> i.get(1))); // 按照第二个数从小到大排列
        List<List<Integer>> ans = new ArrayList<>();
        int forwardLen = forwardRouteList.size(), returnLen = returnRouteList.size();
        int left = 0, right = returnLen - 1;
        int max = Integer.MIN_VALUE;

        while (left < forwardLen && right >= 0) { // forward和return第二个元素相加
            int sum = forwardRouteList.get(left).get(1) + returnRouteList.get(right).get(1);
            if (sum > maxTravelDist) { //如果超出范围，右侧--
                right--;
                continue;
            }
            // forward [2,7][1,8][2,14], return [1,5][2,5][3,10][4,14] //7+14越界，sum=7+10, left++,sum=18
            if (max <= sum) {
                if (max < sum) { // 因为遍历得到的答案肯定从小到大，如果有更大的，直接覆盖
                    ans.clear();
                    max = sum; //max=17
                }
                // 第一次 ans=[2,3] index=2, left++后，max=18，ans变成 【1，3】，第三次变成【3，2】
                ans.add(Arrays.asList(forwardRouteList.get(left).get(0), returnRouteList.get(right).get(0)));
                int index = right;
                // index = right=1, return[0](1) = return[1](1) 有重复的，就向前挪一位 再加一遍
//                while (index - 1 >= 0 && returnRouteList.get(index - 1).get(1) == returnRouteList.get(index).get(1)) {
//                    ans.add(Arrays.asList(forwardRouteList.get(left).get(0), returnRouteList.get(index - 1).get(0)));
//                    index--;
//                }
                while (right - 1 >= 0 && returnRouteList.get(right - 1).get(1) == returnRouteList.get(right).get(1)) {
                    ans.add(Arrays.asList(forwardRouteList.get(left).get(0), returnRouteList.get(right - 1).get(0)));
                    right--;
                }
            }
            left++;
        }

        if (ans.isEmpty()) {
            ans.add(new ArrayList<>());
        }
        return ans;
    }

    public static void main(String[] args) {
        List<List<Integer>> forwardRouteList = new ArrayList<>();
        List<List<Integer>> returnRouteList = new ArrayList<>();
        forwardRouteList.add(Arrays.asList(1,8));
        forwardRouteList.add(Arrays.asList(2,7));
        forwardRouteList.add(Arrays.asList(3,14));
        returnRouteList.add(Arrays.asList(1,5));
        returnRouteList.add(Arrays.asList(2,5));
        returnRouteList.add(Arrays.asList(3,10));
        returnRouteList.add(Arrays.asList(4,14));

        RoutePairs sol = new RoutePairs();
        List<List<Integer>> res = sol.routePairs(20, forwardRouteList, returnRouteList);
        for (List<Integer> r : res) {
            System.out.println(r.get(0) + ", " + r.get(1));
        }
    }
}
