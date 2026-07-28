class Solution:
    def isValid(self, s: str) -> bool:
        o = ["(","[", "{"]
        c = [")","]","}"]

        stack = []

        for b in s:
            if b in o:
                stack.append(b)

            else:
                if len(stack) == 0:
                    return False
                elif b == ")" and stack[-1] == "(":
                    stack.pop()

                elif b == "}" and stack[-1] == "{":
                    stack.pop()

                elif (b == "]" and stack[-1] == "["):
                    stack.pop()

                else:
                    stack.append(b)

        if not stack:
            return True
        else:
            return False
