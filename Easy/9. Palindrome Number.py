class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        palin=0
        y=x

        while y:
            palin=palin*10+y%10
            y //=10

        return palin==x
