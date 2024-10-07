class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum=0
        for i in words:
            temp=list(chars)
            form_flag=True
            for j in i:
                if j in temp:
                    temp.remove(j)
                else:
                    form_flag=False
                    break
            if form_flag:
                sum+=len(i)
        return sum