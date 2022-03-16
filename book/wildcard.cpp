#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*

3
he?p
3
help
heap
helpp
*p*
3
help
papa
hello
*bb*
1
babbbc

*/

void solve(string p, vector<string> m) {
	cout << "start solve with pattern " << p << endl;
	for(auto z : m)
	{
		vector<vector<bool>> dp(z.size() + 1, vector<bool>(p.size() + 1, false));
		dp[0][0] = true;
		for (int i = 1; i <= p.size(); i++)
		{
			if (p[i - 1] == '*')
				dp[0][i] = dp[0][i-1];
			else
				dp[0][i] = false;
		}
		for (int i = 1; i <= z.size(); i++)
			dp[i][0] = false;
		for (int i = 1; i <= z.size(); i++)
		{
			for(int j = 1; j <= p.size(); j++)
			{
				if(p[j - 1] == z[i - 1] || p[j - 1] == '?')
					dp[i][j] = dp[i-1][j-1];
				else if (p[j - 1] == '*')
					dp[i][j] = dp[i-1][j] || dp[i][j-1];
				else
					dp[i][j] = false;
			}
		}
		if (dp[z.size()][p.size()])
			cout << z << endl;
	}
}

int main() {
	int attempt;
	cin >> attempt;
	for (int i = 0; i < attempt; i++)
	{
		string p;
		cin >> p;
		int c;
		cin >> c;
		vector<string> m(c, "");
		for(int j = 0; j < c; j++)
			cin >> m[j];
		solve(p, m);

	}
	return 0;
}