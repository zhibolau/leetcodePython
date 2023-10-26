"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [''] * 4         
        read = 0
        while read < n: 
            count = read4(buf4)             # Read file into buf4 && count -> num of chars in buf4
            if not count: break             # no of chars to read, EOF
            count = min(count, n - read)    # if n = 5 and file size is 8, in second read you have to take only n-read i.e 5-4 = 1
            buf[read:] = buf4[:count]       # Copy from buf4 to buf(destination).
            read += count
        return read 
        