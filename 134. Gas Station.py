class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        index = 0
        gas_rest = 0
        for i in range(len(gas)):
            gas_rest += gas[i] - cost[i]
            if gas_rest < 0:
                gas_rest = 0 #此时说明到不了了 ，从下一个index重新开始 ，所以重置剩余油量
                index =i+ 1
        return index
