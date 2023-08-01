class Solution:
    def matchBrackets(self , a , b):
        if a == '(' and b == ')':
            return True
        if a == '[' and b == ']':
            return True
        if a == '{' and b == '}':
            return True
        
        return False
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # push opening brackets into stack
            if char == '[' or char == '{' or char == '(':
                stack.append(char)
            else:
                # check if the stack is empty and not a opening brackets
                if(len(stack) == 0):
                    return False
                
                # match the brackets
                if(self.matchBrackets(stack[-1],char)):
                    stack.pop()
                else:
                    return False
        # check after the loop , the stack is become empty or not
        return len(stack) == 0