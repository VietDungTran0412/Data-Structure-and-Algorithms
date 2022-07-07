class Solution:
    def __repr__(self) -> str:
        tickets= [5,3,2,7,9]
        return str(self.timeRequiredToBuy(tickets,1))
    def timeRequiredToBuy(self, tickets: list, k : int)->int:
        time = 0 
        for i in range(len(tickets)):
            if i <= k:
                time+= min(tickets[i],tickets[k])
            else:
                time+= min(tickets[i],tickets[k]-1)
        return time
if __name__ == "__main__":
    print(Solution())