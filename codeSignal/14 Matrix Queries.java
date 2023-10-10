// # 014 Matrix Queries
// # given a matrix, n * m
// # the value of each position of this matrix is board[i][j] = (i+1)(j+1)

// # now we have some queries.
// # [0] find the minimum values among all the remaining active cells on board.
// # [1, i] deactivate all the cells in row i
// # [2, j] deactivate all the cells in column j

// # now, return each results when we input an array of queries.
public class matrixQuery {
    public int[] solution(int[][] queries, int m, int n){
        int[] memo = new int[2];
        int minval = Integer.MAX_VALUE;
        //find the minimal, record the value and the position
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if((i+1)*(j+1)<minval){
                    memo[0] = i;
                    memo[1] = j;
                    minval = (i+1)*(j+1);
                }
            }
        }
        Set<Integer> row = new HashSet<>();
        Set<Integer> col = new HashSet<>();
        List<Integer> res = new ArrayList<>();
        for(int[] query: queries){
            if(query.length==1){ //if we only query the remaining minimal
                if(!row.contains(memo[0]) && !col.contains(memo[1])){ //if we don't need to remove the current minimal
                    res.add(minval);
                }else{ //if we have to have to move the minimal, so we need to update it too
                    minval = Integer.MAX_VALUE;
                    for(int i=0; i<m; i++){
                        if(row.contains(i)) continue;
                        for(int j=0; j<n; j++){
                            if(col.contains(j)) continue;
                            if((i+1)*(j+1)<minval){ //update the position of minimal 
                                memo[0] = i; 
                                memo[1] = j;
                                minval = (i+1)*(j+1);
                            }
                        }
                    }
                    res.add(minval);
                }
            }else{ //if we need to deactivate
                if(query[0] == 1){
                    row.add(query[1]-1);
                }else if(query[0] == 2){
                    col.add(query[1]-1);
                }
            }
        }

        int[] result = new int[res.size()];
        for(int i=0; i<res.size(); i++){
            result[i] = res.get(i);
        }
        return result;
    }

    public static void main(String[] args){
        matrixQuery mq = new matrixQuery();
        int[][] queries = new int[][]{{0},{1,2},{0},{2,1},{0},{1,1},{0}};
        int[]res = mq.solution(queries, 3,4);
        for(int i=0; i<res.length; i++){
            System.out.print(res[i]);
            System.out.print(" ");
        }
    }
}

