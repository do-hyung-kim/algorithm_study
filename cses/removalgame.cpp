#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

#define YET 9223372036854775807

long long first_max_dp[5001][5001];
long long second_max_dp[5001][5001];
int lists[5001];

void fillDP(int start, int end)
{
    if (end - start == 0)
        return;
    if (end - start == 1)
    {
        first_max_dp[start][end] = max(lists[start], lists[end]);
        second_max_dp[start][end] = min(lists[start], lists[end]);
        return;
    }
    if(first_max_dp[start+1][end] == YET)
        fillDP(start +1, end);
    if(first_max_dp[start][end-1] == YET)
        fillDP(start, end - 1);
    if (lists[start] + second_max_dp[start+1][end] > lists[end] + second_max_dp[start][end-1])
    {
        first_max_dp[start][end] = lists[start] + second_max_dp[start+1][end];
        second_max_dp[start][end] = first_max_dp[start+1][end];
    }
    else
    {
        first_max_dp[start][end] = lists[end] + second_max_dp[start][end-1];
        second_max_dp[start][end] = first_max_dp[start][end-1];       
    }
}

int main()
{
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    fill(&first_max_dp[0][0], &first_max_dp[n][n], YET);
    fill(&second_max_dp[0][0], &second_max_dp[n][n], YET);
    for(int i = 0; i < n; i++)
    {
        int temp;
        std::cin >> temp;
        lists[i] = temp;
        first_max_dp[i][i] = temp;
        second_max_dp[i][i] = 0;
    }
    fillDP(0,n-1);
    cout << first_max_dp[0][n-1];
}