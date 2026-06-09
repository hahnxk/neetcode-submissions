class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            # print(stones)
            stone_x = stones[-2]
            stone_y = stones[-1]
            if stone_x == stone_y:
                stones.pop(-1)
                stones.pop(-1)
            if stone_x < stone_y:
                stones[-2] = stone_y - stone_x
                stones.pop(-1)
        
        if len(stones) == 0:
            return 0
        else:
            return stones[0]