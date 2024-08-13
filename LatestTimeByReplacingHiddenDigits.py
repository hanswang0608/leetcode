class Solution:
    def maximumTime(self, time: str) -> str:
        output = list(time)
        if output[0] == '?' and output[1] == '?':
            output[0] = '2'
            output[1] = '3'
        if output[0] == '?':
            if int(output[1]) <= 3:
                output[0] = '2'
            else:
                output[0] = '1'
        if output[1] == '?':
            if int(output[0]) == 2:
                output[1] = '3'
            else:
                output[1] = '9'
        if output[3] == '?':
            output[3] = '5'
        if output[4] == '?':
            output[4] = '9'
        return "".join(output)