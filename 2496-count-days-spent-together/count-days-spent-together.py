from datetime import datetime

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a1 = datetime.strptime(arriveAlice, "%m-%d")
        a2 = datetime.strptime(leaveAlice, "%m-%d")
        b1 = datetime.strptime(arriveBob, "%m-%d")
        b2 = datetime.strptime(leaveBob, "%m-%d")

        start = max(a1, b1)
        end = min(a2, b2)

        if start > end:
            return (0)
        else:
            diff = (end - start).days + 1
            return (diff)  