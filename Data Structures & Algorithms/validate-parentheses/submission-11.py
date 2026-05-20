class Solution:
    def isValid(self, s: str) -> bool:
        # Create stack
        stack = []

        # Create dictionary where key: value is close bracket: open bracket
        closeToOpen = { ")": "(",
                        "]": "[",
                        "}": "{"}
        
        # Loop through string
        for c in s:
            # If character is close bracket
            if c in closeToOpen:
                # Check that stack is not empty and has corresponding open bracket as top value
                if stack and stack[-1] == closeToOpen[c]:
                    # If so, remove bracket pairing
                    stack.pop()
                # If fail, return False
                else:
                    return False
            # If character is another open bracket, add it to the top of stack       
            else:
                stack.append(c)
        # True if all characters removed, else False    
        return True if not stack else False

        