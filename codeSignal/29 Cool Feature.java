// 029 Cool Feature
// this problem is relatively simple.
// Given two integer arrays, a and b, as the data needs to be queried.
// and given an array of queries, each query maybe one of the two forms below:

// modify query: [0, i, x] means we need to assign b[i] with the value of x. don’t need to return anything
// calculate query: [1, x] means we have to find the total number of pairs in a and b such that a[i] + b[j] = x. Return the value of the results.
// the return format should be an array of integers, and each element represents the results returned by current query.

// idea: So essentially, this problem is a dynamic query version of two sum.

public class CoolFeature {

    public List<Integer> solution(int[] a, int[] b, int[][] query){
        if(query.length == 0 || query == null) return new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        for(int i: a){
            map.put(i, map.getOrDefault(i, 0)+1);
        } //calcuate the frequency of each element in array a, due to it's a two sum problem, all we need is to store one of those array
        List<Integer> res = new ArrayList<>();
        Map<Integer, Integer> memo = new HashMap<>();
        for(int i=0; i<query.length; i++){ //
            int[] temp = query[i];
            if(temp.length == 3){ //[0, i, x]
                b[temp[1]] = temp[2];
            }else{ //[1, x]
                int sum = query[i][1];
                int count = 0;
                for(int j=0; j<b.length; j++){ //the core of two sum
                    int target = sum-b[j];
                    if(map.containsKey(target)){
                        count+=map.get(target);
                    }
                }
                res.add(count);
            }
        }
        return res;
    }



    public static void main(String[] args){
        CoolFeature cf = new CoolFeature();
        int[] A = {1,1,2,3};
        int[] B = {1,1};
        int[][] query = {{1,5}, {1,0,1}, {1,5},{1,7}};
        System.out.print(cf.solution(A,B, query));
    }
}


