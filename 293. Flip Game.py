class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        return [s[:i] + '--' + s[i+2:] for i in range(len(s) - 1) if s[i:i+2] == '++']
