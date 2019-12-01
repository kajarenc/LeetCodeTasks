class Solution:
    def decodeString(self, s: str) -> str:
        n  = len(s) 
        if '[' not in s:
            return s
        i = 0
        while not s[i].isdigit():
            i += 1
        number = 0
        number_index = i

        while s[i].isdigit():
            number = number * 10 + int(s[i])
            i += 1

        open_ = i
        balance = 1
        i += 1

        while balance != 0 and i < n:
            if s[i] == '[':
                balance += 1
            elif s[i] == ']':
                balance -= 1
            i += 1

        close_ = i - 1

        new_str = s[:number_index] + number*self.decodeString(s[open_+1:close_]) + self.decodeString(s[close_+1:])
        return new_str
