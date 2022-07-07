class Solution:
    def __repr__(self) -> str:
        return str([self.fib(7),self.dynamicProgrammingFib(7)])
    def fib(self,n):
        if n == 1 or n == 2:
            return 1
        return self.fib(n-1)+self.fib(n-2)
    def dynamicProgrammingFib(self,n,ar = [0,1]):
        if n <= 0:
            return 0
        elif n < len(ar):
            return ar[n]
        else:
            ar.append(self.dynamicProgrammingFib(n-1)+self.dynamicProgrammingFib(n-2))
            return ar[n]
if __name__ == "__main__":
    print(Solution())
        