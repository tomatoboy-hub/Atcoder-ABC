#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    ll L,Q;
    cin >> L >> Q;
    set<ll> S;
    S.insert(0);
    S.insert(L);
    ll c, x;
    for (int i = 0; i < Q; i++){
        cin >> c >> x;
        if (c == 1){
            S.insert(x);
        } else {
            auto it = S.lower_bound(x);
            ll l = *prev(it);
            ll r = *it;
            cout << (r - l) << endl;
        }
    }
}