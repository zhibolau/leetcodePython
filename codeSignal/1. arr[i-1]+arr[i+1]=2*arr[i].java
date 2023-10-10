# 001 给一串int[] 找出所有arr[i-1]+arr[i+1]=2*arr[i]的情况


# idea: from the index1 to indexlength-2, iterate everything

if arr.length <= 2 return nothing
int i = 1;
while (i <= arr.length - 2) {
if (arr[i-1]+arr[i+1] == 2*arr[i]) {
//
}
}
return

we can’t use presort because order matters.
this O(n) solution is good enough.
