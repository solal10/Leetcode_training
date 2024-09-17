class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lists1=s1.split()
        lists2=s2.split()
        word_count = Counter(lists1) + Counter(lists2)
        print(word_count)
        return [word for word, count in word_count.items() if count == 1]
        