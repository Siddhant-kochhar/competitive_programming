#include <bits/stdc++.h>
using namespace std;

int cardValue(string s) {
    if (s == "A") return 1;
    if (s == "J") return 11;
    if (s == "Q") return 12;
    if (s == "K") return 13;
    return stoi(s);
}

int suitRank[5];

bool cmp(pair<int,int> a, pair<int,int> b) {
    if (a.first != b.first) return a.first < b.first;
    return suitRank[a.second] > suitRank[b.second];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<pair<int,int>> v1, v2;
    for (int i = 0; i < n; i++) {
        string c1, c2;
        int s1, s2;
        cin >> c1 >> s1 >> c2 >> s2;
        v1.push_back({cardValue(c1), s1});
        v2.push_back({cardValue(c2), s2});
    }

    for (int i = 0; i < 4; i++) {
        int x; cin >> x;
        suitRank[x] = i;
    }

    sort(v1.begin(), v1.end(), cmp);
    sort(v2.begin(), v2.end(), cmp);

    deque<pair<int,int>> d1(v1.begin(), v1.end()), d2(v2.begin(), v2.end());
    vector<pair<int,int>> pile;
    bool turn1 = true;

    while (true) {
        if (turn1) {
            if (d1.empty()) {
                if (d2.empty()) cout << "TIE";
                else cout << "LOSER";
                return 0;
            }
            auto card = d1.front(); d1.pop_front();
            if (pile.empty()) {
                pile.push_back(card);
                turn1 = false;
            } else {
                auto top = pile.back();
                if (card.first == top.first && suitRank[card.second] < suitRank[top.second]) {
                    pile.push_back(card);
                    sort(pile.begin(), pile.end(), cmp);
                    for (auto &x : pile) d1.push_back(x);
                    pile.clear();
                } else {
                    pile.push_back(card);
                    turn1 = false;
                }
            }
        } else {
            if (d2.empty()) {
                if (d1.empty()) cout << "TIE";
                else cout << "WINNER";
                return 0;
            }
            auto card = d2.front(); d2.pop_front();
            if (pile.empty()) {
                pile.push_back(card);
                turn1 = true;
            } else {
                auto top = pile.back();
                if (card.first == top.first && suitRank[card.second] < suitRank[top.second]) {
                    pile.push_back(card);
                    sort(pile.begin(), pile.end(), cmp);
                    for (auto &x : pile) d2.push_back(x);
                    pile.clear();
                } else {
                    pile.push_back(card);
                    turn1 = true;
                }
            }
        }
    }
}