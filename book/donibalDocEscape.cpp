#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int c, n, d, p, q;
    cin >> c;
    for (;c>0;c--)
    {
        int connected[51][51], deg[51], vill[51];
        double dp[101][51] = {0, };
        cin >> n >> d >> p;
        for (int i = 0; i<n; i++)
        {
            int deg_num = 0;
            for (int j = 0; j<n; j++)
            {
                cin >> connected[i][j];
                if(connected[i][j] == 1)
                    deg_num++;
            }
            deg[i] = deg_num;
        }
        cin >> q;
        for (int i = 0; i < q; i++)
            cin >> vill[i];
        for(int i = 0; i < d; i++)
        {
            if(i == 0)
            {
                for(int j = 0; j < n; j++)
                {
                    if(connected[p][j] == 1)
                    {
                        dp[i][j] = 1 / (double) deg[p];
                    }
                }
                continue;
            }
            else
            {
                for(int j = 0; j < n; j++)
                {
                    for(int k = 0; k < n; k++)
                    {
                        if(connected[j][k])
                            dp[i][j] += dp[i-1][k] * (1 / (double) deg[k]);
                    }
                }
            }
        }
        for (int i = 0; i<q; i++)
            cout << setprecision(8) << dp[d-1][vill[i]]  << " ";
    }
}
