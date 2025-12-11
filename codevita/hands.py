from collections import deque

def cardValue(s: str) -> int:
    """Convert card face to numeric value."""
    if s == "A": return 1
    if s == "J": return 11
    if s == "Q": return 12
    if s == "K": return 13
    return int(s)

def main():
    import sys
    input = sys.stdin.readline  # faster input

    n = int(input())
    v1, v2 = [], []

    for _ in range(n):
        c1, s1, c2, s2 = input().split()
        s1, s2 = int(s1), int(s2)
        v1.append((cardValue(c1), s1))
        v2.append((cardValue(c2), s2))

    suitRank = [0] * 5
    for i in range(4):
        x = int(input())
        suitRank[x] = i

    # Precompute sorting key for speed
    def sort_key(x):
        return (x[0], -suitRank[x[1]])

    v1.sort(key=sort_key)
    v2.sort(key=sort_key)

    d1 = deque(v1)
    d2 = deque(v2)
    pile = []
    turn1 = True

    append_pile = pile.append
    clear_pile = pile.clear
    extend_d1 = d1.extend
    extend_d2 = d2.extend

    while True:
        if turn1:
            if not d1:
                print("TIE" if not d2 else "LOSER")
                return
            card = d1.popleft()

            if not pile:
                append_pile(card)
                turn1 = False
            else:
                top = pile[-1]
                if card[0] == top[0] and suitRank[card[1]] < suitRank[top[1]]:
                    append_pile(card)
                    pile.sort(key=sort_key)
                    extend_d1(pile)
                    clear_pile()
                else:
                    append_pile(card)
                    turn1 = False

        else:
            if not d2:
                print("TIE" if not d1 else "WINNER")
                return
            card = d2.popleft()

            if not pile:
                append_pile(card)
                turn1 = True
            else:
                top = pile[-1]
                if card[0] == top[0] and suitRank[card[1]] < suitRank[top[1]]:
                    append_pile(card)
                    pile.sort(key=sort_key)
                    extend_d2(pile)
                    clear_pile()
                else:
                    append_pile(card)
                    turn1 = True


if __name__ == "__main__":
    main()