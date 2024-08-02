#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

int main() {
    using namespace std;
    int N;
    string S;
    cin >> N >> S;
    ranges::sort(S);

    long max_value = pow(10,N);
    int ans = 0;
    for (long i = 0; i*i < max_value; ++i){
        string T = to_string(i*i);
        ranges::sort(T);
        if (S == T) ++ans;
    }
    cout << ans << endl;

    return 0;

}