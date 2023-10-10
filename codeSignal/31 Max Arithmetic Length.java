// 031 Max Arithmetic Length(Hard, not understand at all)

// given two arrays a and b, they contains no duplicated and it is sorted.

// now the rules are:
// we can pick any elements from b, and all the picked elements, we need to insert them in a such that all the elements in a are increasing in by certain number, like a Arithmetic sequence.
// now we need to write a function to return the maximum number in a after appending elements from b. if there is no such case, then we just need to return -1.

// idea:
// brute force: let find out what a needs, if it has more than 1 element, then the sequence is determined(but the length of that determined by b), if a has only one element, then still, b will determine the final length.
// but even brute force can’t makes this problem easier, like how to extract numbers we need from b and how do we know it is the longest?(maybe for situation 1, there only exist one sequence that satisfied the needs, but for situation 2, there might exist more than one sequences)


public class maxArithmeticLength {
    public maxArithmeticLength() {
    }

    public static void addAfter(int[] b, int idxB, int diff, LinkedList<Integer> temp) {
        for(; idxB < b.length; ++idxB) {
            if (b[idxB] == diff + (Integer)temp.get(temp.size() - 1)) {
                temp.add(b[idxB]);
            }
        }

    }

    public static void addFront(int[] b, int idxB, int diff, LinkedList<Integer> temp) {
        for(; idxB >= 0; --idxB) {
            if (b[idxB] == (Integer)temp.get(0) - diff) {
                temp.addFirst(b[idxB]);
            }
        }

    }

    public static int checkIdxA(int[] a, int idxA, int diff, LinkedList<Integer> temp) {
        while(idxA < a.length && a[idxA] == diff + (Integer)temp.get(temp.size() - 1)) {
            temp.add(a[idxA++]);
        }

        return idxA;
    }

    public static int findLong(int[] b, int val, int pos, int loc) {
        LinkedList<Integer> temp = new LinkedList();
        temp.add(val);
        int diff = Math.abs(val - b[loc]);
        int res = 0;
        if (pos == -1) {
            addAfter(b, 0, diff, temp);
        } else if (pos == b.length - 1) {
            addFront(b, b.length - 1, diff, temp);
        } else {
            addAfter(b, pos, diff, temp);
            addFront(b, pos, diff, temp);
        }

        int res = Math.max(res, temp.size());
        return res;
    }

    public static int maxArithmeticLength(int[] a, int[] b) {
        int lenA = a.length;
        int lenB = b.length;
        int left = 0;
        int right = lenB - 1;
        int pos = -1;

        int res;
        while(left <= right) {
            res = (right + left) / 2;
            if (b[res] >= a[0]) {
                right = res - 1;
            } else {
                pos = res;
                left = res + 1;
            }
        }

        res = -1;
        int diffMax;
        if (a.length == 1) {
            for(diffMax = 0; diffMax < b.length; ++diffMax) {
                res = Math.max(res, findLong(b, a[0], pos, diffMax));
            }
        } else {
            diffMax = a[1] - a[0];

            int diff;
            for(diff = 1; diff < lenA; ++diff) {
                diffMax = Math.min(diffMax, a[diff] - a[diff - 1]);
            }

            for(diff = 0; diff <= diffMax; ++diff) {
                LinkedList<Integer> temp = new LinkedList();
                temp.add(a[0]);
                int idxA;
                int idxB;
                if (pos == -1) {
                    idxA = 1;
                    idxB = 0;

                    while(idxA < lenA && idxB < lenB) {
                        if (a[idxA] == diff + (Integer)temp.get(temp.size() - 1)) {
                            temp.add(a[idxA++]);
                        } else if (b[idxB] == diff + (Integer)temp.get(temp.size() - 1)) {
                            temp.add(b[idxB++]);
                        } else {
                            ++idxB;
                        }
                    }

                    idxA = checkIdxA(a, idxA, diff, temp);
                    if (idxA == lenA) {
                        addAfter(b, idxB, diff, temp);
                    }
                } else if (pos == lenB - 1) {
                    int idxA = 1;
                    idxA = checkIdxA(a, idxA, diff, temp);
                    if (idxA == lenA) {
                        addFront(b, b.length - 1, diff, temp);
                    }
                } else {
                    idxA = 1;
                    idxB = pos + 1;

                    while(idxA < lenA && idxB < lenB) {
                        if (a[idxA] == diff + (Integer)temp.get(temp.size() - 1)) {
                            temp.add(a[idxA++]);
                        } else if (b[idxB] == diff + (Integer)temp.get(temp.size() - 1)) {
                            temp.add(b[idxB++]);
                        } else {
                            ++idxB;
                        }
                    }

                    idxA = checkIdxA(a, idxA, diff, temp);
                    if (idxA == lenA) {
                        addFront(b, pos, diff, temp);
                        addAfter(b, idxB, diff, temp);
                    }
                }

                res = Math.max(res, temp.size());
            }
        }

        return res;
    }
}

