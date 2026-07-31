class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.cur.next = new_node
        new_node.prev = self.cur
        self.cur = new_node

    def back(self, steps: int) -> str:

        while steps > 0 and self.cur.prev != None:
            self.cur = self.cur.prev
            steps -= 1
        
        return self.cur.val

    def forward(self, steps: int) -> str:
        
        while steps > 0 and self.cur.next != None:
            self.cur = self.cur.next
            steps -= 1

        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)