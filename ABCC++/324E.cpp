#include <iostream>
#include <algorithm>

using namespace std;
typedef long long ll;

ll n;
string s[500001],t;
ll a[500001],b[500001],c[500001];

ll calc(const string &s, const string &t)
{
    ll g = 0;
    for(auto c : s){
        if ( g >= (int)t.size()) break;
        if ( c == t[g] ) g++;
    }

}