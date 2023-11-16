class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
                # Write your code here
        room=[]
        #加入开始时间和结束时间，1是房间+1，-1是房间-1
        for i in intervals:
            room.append((i[0],1))
            room.append((i[1],-1))
        tmp=0
        ans=0
        #排序
        room=sorted(room)
        #扫描一遍
        for idx,cost in room:
            tmp+=cost
            ans=max(ans,tmp)
        return ans