class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character in ["{", "[", "("]:
                stack.append(character)
            elif character in ["}", "]", ")"]:
                if len(stack) > 0 and ((character == "}" and stack[-1] == "{") or \
                    (character == "]" and stack[-1] == "[") or \
                    (character == ")" and stack[-1] == "(")):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0: 
            return False
        return True