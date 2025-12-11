'''
days = 10, meetings = [[5,7],[1,3],[9,10]]

'''

days = 6
meetings = [[1,6]]

meetings.sort(key=lambda x:x[0])
print(meetings)
current_start, current_end = meetings[0]

no_meeting = max(0, current_start - 1)

if len(meetings) > 1:
    for start, end in meetings[1:]:
        x, y = current_start, current_end
        # print(x,y)
        # print(start,y)
        if start > y:
            no_meeting += abs(start-y) -1 
            current_start , current_end = start , end 
        else:
            y = max(current_end,end)

    no_meeting += max((0,abs(end-days)))
    print(no_meeting)
    

else:
    print(days-meetings[0][1])
