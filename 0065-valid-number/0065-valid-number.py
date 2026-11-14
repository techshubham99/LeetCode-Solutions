class Solution:
    def isNumber(self, s: str) -> bool:

        num_seen = False
        dot_seen = False
        e_seen = False
        num_after_e = True

        for i in range(len(s)):
            ch = s[i]

            if '0' <= ch <= '9':
                num_seen = True

                if e_seen:
                    num_after_e = True

            elif ch == '.':
                if dot_seen or e_seen:
                    return False

                dot_seen = True

            elif ch == 'e' or ch == 'E':
                if e_seen or not num_seen:
                    return False

                e_seen = True
                num_after_e = False

            elif ch == '+' or ch == '-':
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            else:
                return False

        return num_seen and num_after_e