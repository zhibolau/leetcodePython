// 027Min Peak
// we are given an array of positive integers, called “numbers”.
// now our task is to consecutively remove the minimal peaks of the given array one by one, and then return an array that contains the removed data in its removal order.

// remember, we will keep this process until there is nothing to remove in our original array.

public class deleteminimalpeaks {
    public deleteminimalpeaks() {
    }

    public List<Integer> solution(int[] array) {
        // List<Integer> list = new ArrayList();
        // List<Integer> res = new ArrayList();
        // int[] var4 = array;
        int val = array.length;

        // int i;
        // for(i = 0; i < val; ++i) {
        //     int num = var4[i];
        //     list.add(num);
        // }

        List<Integer> list = new ArrayList<>();
        List<Integer> res = new ArrayList<>();

        for (int i: array) {
          list.add(i);
        }

        while(!list.isEmpty()) {
            if (list.size() == 1) {
                res.add(list.get(0));
                break;
            }

            int index = 0;
            val = 2147483647;

            for(i = 0; i < list.size(); ++i) { //iterate every element in the list
                if (i == 0) {
                    if ((Integer)list.get(i) >= (Integer)list.get(i + 1) && (Integer)list.get(i) <= val) {
                        index = i;
                        val = (Integer)list.get(i);
                    }
                } else if (i == list.size() - 1) {
                    if ((Integer)list.get(i) >= (Integer)list.get(i - 1) && (Integer)list.get(i) <= val) {
                        index = i;
                        val = (Integer)list.get(i);
                    }
                } else if ((Integer)list.get(i) >= (Integer)list.get(i - 1) && (Integer)list.get(i) >= (Integer)list.get(i + 1) && (Integer)list.get(i) <= val) {
                    index = i;
                    val = (Integer)list.get(i);
                }
            }

            list.remove(index);
            res.add(val);
        }

        return res;
    }

    public static void main(String[] args) {
        deleteminimalpeaks dm = new deleteminimalpeaks();
        int[] array = new int[]{1, 2};
        System.out.print(dm.solution(array));
    }
}

