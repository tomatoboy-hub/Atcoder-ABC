#include <bits/stdc++.h> 
using namespace std;
using ll = long long;
constexpr ll INF64 = (1LL << 62) - 1;

struct fast_ios{
    fast_ios(){
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        cout << fixed << setprecision(15);
    }
} fast_ios;

int main(){
    int Q; 
    cin >> Q;
    ll q,x,k;
    multiset<ll> S;
    for (int i = 0; i < 5; ++i){
        S.insert(-INF64);
        S.insert(INF64);
    }

    for (int i = 0; i < Q; ++i){
        cin >> q >> x;
        if (q == 1){
            S.insert(x);
        }
        if (q == 2){
            cin >> k;
            auto it = S.upper_bound(x);
            for (int j = 0; j < k; j++){ --it;} 
            ll ans = *it != -INF64 ? *it : -1;
            cout << ans << '\n';
        }
        if (q == 3){
            cin >> k;
            auto it = S.lower_bound(x);
            for(int j = 0; j < k - 1; j++){ ++it };
            ll ans = *it != INF64 ? *it : -1;
            cout << ans << '\n';
        }
    }
}