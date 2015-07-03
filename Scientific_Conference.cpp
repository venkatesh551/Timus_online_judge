#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> pii;

bool sort_pred(const pii& left, const pii& right)
{
    return left.second < right.second;
}

int main()
{
    int n;
    cin >> n;
    vector<pii> v(n);
    for (int i = 0; i < n; ++i)
    {
        int x, y;
        cin >> x >> y;
        v[i] = make_pair(x, y);
    }
    sort(v.begin(), v.end(), sort_pred);
    int last = 0, cnt = 0;
    for (int i = 0; i < n; ++i)
    {
        if (v[i].first > last)
        {
            last = v[i].second;
            cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}
