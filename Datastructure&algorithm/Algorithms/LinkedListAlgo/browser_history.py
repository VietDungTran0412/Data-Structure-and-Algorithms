class Page:
    def __init__(self,url: str) -> None:
        self.url = url
        self.prev = None
        self.next = None
class BrowserHistory:
    def __init__(self, homepage: str) -> None:
        self.head = Page(homepage)
        self.cur = self.head
    def visit(self,url: str)-> None:
        newPage = Page(url)
        newPage.prev = self.cur
        self.cur.next = newPage
        self.cur = self.cur.next
    def back(self, steps: int)-> str:
        count = 0
        while self.cur.prev and count < steps:
            self.cur = self.cur.prev
            count +=1
        return self.cur.url
    def forward(self,steps: int)-> str:
        count = 0
        while self.cur.next and count < steps:
            self.cur = self.cur.next
            count +=1
        return self.cur.val
if __name__ == "__main__":
    obj = BrowserHistory("a")
    ar = ["b","c","d"]
    for url in ar:
        obj.visit(url)
    print(obj.back(3))