#include <iostream>
#include <vector>

using namespace std;

/**
7
2 5 1 6 1 4 1
6 1 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 2
4 1 2 3 4 1 2
3 3 1 2 3 4 1
1 5 2 9 4 7 0

7
2 5 1 6 1 4 1
6 1 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 2
4 1 2 3 4 1 3
3 3 1 2 3 4 1
1 5 2 9 4 7 0

7
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 2
1 1 1 1 1 2 0

*/

int main() {
    int n;
    cin >> n;
    vector<vector<int>> input(n, vector<int>(n, 0));
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    dp[0][0] = true;
    for(int i = 0; i  < n; i++)
        for(int j = 0; j < n; j++)
            cin >> input[i][j];

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if (dp[i][j])
            {
                if(i + input[i][j] < n)
                    dp[i+input[i][j]][j] = true;
                if(j + input[i][j] < n)
                    dp[i][j + input[i][j]] = true;
            }
        }
    }
    if (dp[n-1][n-1]) cout<< "TRUE"<<endl;
    else cout << "FALSE" <<endl;

    return 0;
}