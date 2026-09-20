class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair = { 
        ')':'(',
        '}':'{',
        ']':'[' 
        }
        my_open_stack = []

        for cur_bracket in range(len(s)):
            # handle open bracket
            if s[cur_bracket] not in valid_pair:
                my_open_stack.append(s[cur_bracket])

            # handle close bracket
            else: 
                if not my_open_stack or my_open_stack.pop() != valid_pair[s[cur_bracket]]:
                    return False
        return not my_open_stack 