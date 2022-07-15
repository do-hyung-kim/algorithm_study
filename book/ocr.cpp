#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string words[501];
int m, q, n;
int R[100];
double T[501][501]; // i 다음 j가 나올 확률
double M[501][501]; // i 가 j로 인식될 확률
int choice[102][502];
double memo[102][502]; // dp

double findMaxPercent(int segmentNum, int prevChar)
{
    if (segmentNum == m)
        return 0;
    double& ret = memo[segmentNum][prevChar];
    if (ret != 1.0) return ret;
    ret = -1e200;
    int& pick = choice[segmentNum][prevChar];
    for (int matchOne = 1; matchOne <= m; ++matchOne)
    {
        double temp = T[prevChar][matchOne] + M[matchOne][R[segmentNum]] + findMaxPercent(segmentNum + 1, matchOne);
        if (temp > ret)
        {
            ret = temp;
            pick = matchOne;
        }
    }
    return ret;
}

string reconstruct(int segmentNum, int prevChar)
{
    int pick = choice[segmentNum][prevChar];
    string ret = words[pick];
    if (segmentNum < n-1)
        ret = ret + " " + reconstruct(segmentNum + 1, pick);
    return ret;
}

int main()
{
    cin >> m >> q;
    for(int i = 1; i<=m; i++)
        cin >> words[i];
    for (int i = 0; i <= m; i++)
        for (int j = 1; j <= m; j++)
        {
            cin >> T[i][j];
            T[i][j] = log(T[i][j]);
        }
    for (int i = 1; i<=m; i++)
    {
        for (int j = 1; j <=m; j++)
        {
            cin >> M[i][j];
            M[i][j] = log(M[i][j]);
        }
    }
    
    for (int i = 0; i < q; i++)
    {
        cin >> n;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                memo[i][j] = 1.0;
        for (int i = 0; i < n; i++)
        {
            string input;
            cin >> input;
            for (int j = 1; j <= m; j++)
            {
                if (input == words[j])
                {
                    R[i] = j;
                    break;
                }
            }
        }
        findMaxPercent(0, 0);
        cout << reconstruct(0,0) << endl;
    }
}

