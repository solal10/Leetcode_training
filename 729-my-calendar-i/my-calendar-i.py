class MyCalendar:

    def __init__(self):
        self.rdv=[]

    def book(self, start: int, end: int) -> bool:
        for interval in self.rdv:
            if not (end <= interval[0] or start >= interval[1]):
                return False
        self.rdv.append([start,end])
        return True
                
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)