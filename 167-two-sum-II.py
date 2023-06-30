class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) -1
        sum = 0

        while start<end:
            sum = numbers[start]+numbers[end]
            if sum < target:
                start +=1
            elif sum == target:
                break
            else:
                end -=1
        return [start+1, end+1]
