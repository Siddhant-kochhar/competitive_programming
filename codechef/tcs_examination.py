'''
4
10 20 30
30 20 10
5 23 87
5 23 87
0 15 100
100 5 5
50 50 50
50 49 51
'''

t = int(input())

for _ in range(t):
    d,t,m = map(int,input().split())
    d_2,t_2,m_2 = map(int,input().split())

    if d+t+m > d_2+t_2+m_2:
        print("DRAGON")
        break
    elif d+t+m < d_2+t_2+m_2:
        print("SLOTH")
        break
    elif d+t+m == d_2+t_2+m_2 and d > d_2:
        print("DRAGON")
        break
    elif d+t+m == d_2+t_2+m_2 and d < d_2:
        print("SLOTH")
        break
    elif d+t+m == d_2+t_2+m_2 and d == d_2 and t > t_2:
        print("DRAGON")
        break
    elif d+t+m == d_2+t_2+m_2 and d == d_2 and t < t_2:
        print("SLOTH")
        break
    else:
        print("TIE")
        break