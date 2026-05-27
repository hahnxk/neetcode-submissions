class Solution:
    def isValid(self, s: str) -> bool:
        # Stacks in python can be implemented using lists
        # Methods: append(), pop(), peak()

        # Idea: Use a stack data structure to keep track of string characters and
        #       use a dictionary to create pairs between different bracket types
        # 1. Create a dictionary where (key, value) is (close bracket, open bracket)
        # 2. Loop through string
        # 3. If character in dictionary (i.e. is close bracket), pop from stack and check
        #    if dict[character] == popped item. If so, do nothing, else return False.
        # 4. If character not in dictionary (i.e. is open bracket), add to the stack
        # Once looped, if stack is empty, return True, else return False

        stack = []
        s_dict = {")": "(",
                  "}": "{",
                  "]": "["}

        for c in s:
            if c in s_dict:
                if stack and stack[-1] == s_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) != 0:
            return False
        return True
