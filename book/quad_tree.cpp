#include <iostream>
#include <string>

using namespace std;

/*

4
w
xbwwb
xbwxwbbwb
xxwwwbxwxwbbbwwxxxwwbbbwwwwbb

w
xwbbw
xxbwwbbbw
xxwbxwwxbbwwbwbxwbwwxwwwxbbwb

*/

string reverse(string::iterator& it) {
    char head = *it;
    ++it;
    if (head == 'b' || head == 'w')
        return string(1, head);
    string UL = reverse(it);
    string UR = reverse(it);
    string LL = reverse(it);
    string LR = reverse(it);

    return string("x") + LL + LR + UL + UR;
}

int main() {
    int cnt = 0;
    cin >> cnt;
    string inputs[cnt];
    for (int i = 0; i < cnt; i++)
    {
        cin >> inputs[i];
    }
    for(int i = 0; i < cnt; i++)
    {
        string::iterator iter = inputs[i].begin();
        cout << reverse(iter) << endl;
    }
    return 0;
}