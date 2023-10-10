// 019 Check ABC(longest subarray check)


// we are given three array of integers.
// let say a, b and c
// c is an array with distinct integers.
// now we need to check whether b is the longest subarray of a consisting only of elements from c.

// the means:
// each element of b must belongs to c
// b is a subarray of a.
// then from all the b that satisfy the previous, get the longest one.
// if that one is the same as b, then return true

// //the following code is not exactly the same as the solution should be. but apart from inputs are integer array instead of string
// ————————————————



public class longestsubarray {
    public longestsubarray() {
    }

    public boolean solution(String a, String b, String c) {
        Set<Character> set = new HashSet();
        char[] var5 = c.toCharArray();
        int len = var5.length;

        int var7;
        char element;
        for(var7 = 0; var7 < len; ++var7) {
            element = var5[var7];
            set.add(element);
        }

        var5 = b.toCharArray();
        len = var5.length;

        for(var7 = 0; var7 < len; ++var7) {
            element = var5[var7];
            if (!set.contains(element)) {
                return false;
            }
        }

        if (b.length() > a.length()) {
            return false;
        } else {
            String res = "";
            len = b.length();
            int[] pos = new int[2];

            for(int i = 0; i <= a.length() - len; ++i) {
                String substring = a.substring(i, i + len);
                if (substring.equals(b)) {
                    res = substring;
                    pos[0] = i - 1;
                    pos[1] = i + len;
                }
            }

            if (res == "") {
                return false;
            } else {
                if (pos[0] == -1 || pos[1] == a.length()) {
                    if (pos[0] == -1 && pos[1] == a.length()) {
                        return true;
                    }

                    if (pos[0] == -1) {
                        return !set.contains(a.charAt(pos[1]));
                    }

                    if (pos[1] == a.length()) {
                        return !set.contains(a.charAt(pos[0]));
                    }
                }

                return !set.contains(a.charAt(pos[0])) && !set.contains(a.charAt(pos[1]));
            }
        }
    }

    public static void main(String[] args) {
        String a = "cccbbaab";
        String b = "cccbbaab";
        String c = "abc";
        longestsubarray ls = new longestsubarray();
        System.out.print(ls.solution(a, b, c));
    }
}

