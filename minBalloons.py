class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        record_of_letters = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for i in text:
            if i in record_of_letters:
                record_of_letters[i] += 1
        num = True
        while num:
            for key in record_of_letters:
                if key == 'b':
                    record_of_letters['b'] -= 1
                    if record_of_letters['b'] < 0:
                        num = False
                        break
                elif key == 'a':
                    record_of_letters['a'] -= 1
                    if record_of_letters['a'] < 0:
                        num = False
                        break
                elif key == 'l':
                    record_of_letters['l'] -= 2
                    if record_of_letters['l'] < 0:
                        num = False
                        break
                elif key == 'o':
                    record_of_letters['o'] -= 2
                    if record_of_letters['o'] < 0:
                        num = False
                        break
                else:
                    record_of_letters['n'] -= 1
                    if record_of_letters['n'] < 0:
                        num = False
                        break
            count += 1
        return count - 1
