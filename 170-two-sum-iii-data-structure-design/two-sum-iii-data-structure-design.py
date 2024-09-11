class TwoSum:

    def __init__(self):
        self.num_count={}

    def add(self, number: int) -> None:
        if number in self.num_count:
            self.num_count[number]+=1
        else:
            self.num_count[number]=1

    def find(self, value: int) -> bool:
        for number in self.num_count:
            complement = value-number
            if complement in self.num_count:
                if complement == number and self.num_count[number]>1:
                    return True
                if complement !=number:
                    return True
        return False
            

        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)