from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                # If the token is a number, push it onto the stack
                stack.append(int(token))
            else:
                # Pop the last two numbers from the stack
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation based on the token
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Perform integer division, truncating toward zero
                    # Use int() to handle truncation correctly
                    stack.append(int(a / b))  # Division should truncate towards zero
        
        # The result will be the last element in the stack
        return stack.pop()

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))       # Output: 9
    print(solution.evalRPN(["4", "13", "5", "/", "+"]))      # Output: 6
    print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # Output: 22
