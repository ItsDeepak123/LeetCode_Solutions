class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones=10
        Alise=True
        while n>=stones:
            n-=stones
            stones-=1
            Alise=not Alise

        return not Alise
            