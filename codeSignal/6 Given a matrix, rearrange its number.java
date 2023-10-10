// 006 Given a matrix, rearrange its number

// first, sort the values in this matrix by its frequency. if there is a tie, then order them by their values.
// then, place the sorted number diagonally, starting from the bottom right corner, like the following:
// 5 4 4
// 4 4 3
// 3 2 1

// brute force:
// first we sort them, then we put the back by the order of “right bottom to left top”

public class sortmatrixByoccurance {
    public void solution(int[][] matrix){
        Map<Integer, Integer> map = new HashMap<>(); //using hashmap to store it's proficiency
        int m = matrix.length;
        int n = matrix[0].length;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                map.put(matrix[i][j], map.getOrDefault(matrix[i][j],0)+1); 
            }
        }

        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet()); //sort the entry set of this map by the frequency and value
        Collections.sort(list, new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                if(o1.getValue() == o2.getValue()){
                    return o1.getKey().compareTo(o2.getKey());
                }else{
                    return o1.getValue().compareTo(o2.getValue());
                }
            }
        });
        int index = 0;
        for(int i=m-1; i>=0; i--){
            for(int j=n-1; j>=0; j--){ //? confused here
                matrix[i][j] = list.get(index).getKey();
                list.get(index).setValue(list.get(index).getValue()-1);
                if(list.get(index).getValue() == 0){
                    index++;
                }
            }
        }

    }

    public static void main(String[] args){
        sortmatrixByoccurance sb = new sortmatrixByoccurance();
        int[][] matrix = new int[][]{{2,2,3,3},{1,1,1,2},{2,2,4,4},{9,10,11,12}};
        sb.solution(matrix);
        for(int i=0; i<matrix.length; i++){
            for(int j=0; j<matrix[0].length; j++){
                System.out.print(matrix[i][j]);
                System.out.print(" ");
            }
            System.out.print("\n");
        }
    }
}

