class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        result=[]
        for i, char in enumerate(expression):
            if char in "+-*":
                left_results=self.diffWaysToCompute(expression[:i])
                right_results=self.diffWaysToCompute(expression[i+1:])
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            result.append(left + right)
                        elif char == '-':
                            result.append(left - right)
                        elif char == '*':
                            result.append(left * right)
        return result
