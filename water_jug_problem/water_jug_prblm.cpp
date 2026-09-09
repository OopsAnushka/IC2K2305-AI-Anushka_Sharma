#include <iostream>
#include <queue>
#include <set>
#include <vector>
using namespace std;

struct State {
    int a, b;
};

void waterJug(int m, int n, int target) {
    queue<State> q;
    set<pair<int, int>> visited;

    q.push({0, 0});
    visited.insert({0, 0});

    while (!q.empty()) {
        State current = q.front();
        q.pop();

        int a = current.a;
        int b = current.b;

        cout << "(" << a << ", " << b << ")" << endl;

        if (a == target || b == target) {
            cout << "Target reached!" << endl;
            return;
        }

        vector<State> next = {
            {m, b},                         // Fill jug A
            {a, n},                         // Fill jug B
            {0, b},                         // Empty jug A
            {a, 0},                         // Empty jug B
            {a - min(a, n - b), b + min(a, n - b)}, // A -> B
            {a + min(b, m - a), b - min(b, m - a)}  // B -> A
        };

        for (State s : next) {
            if (visited.find({s.a, s.b}) == visited.end()) {
                visited.insert({s.a, s.b});
                q.push(s);
            }
        }
    }

    cout << "Target cannot be measured." << endl;
}

int main() {
    int m = 4, n = 3, target = 2;

    waterJug(m, n, target);

    return 0;
}