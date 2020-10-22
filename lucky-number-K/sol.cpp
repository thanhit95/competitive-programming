// by Nguyen Trung Thanh       https://www.facebook.com/thanh.it95

#include <iostream>
#include <cmath>
#include <bitset>
#include <string>
using namespace std;


int getLog2(int K)
{
    // return log2(K);
    int i = 0;

    while (K >>= 1)
        ++i;

    return i;
}


string getResult(const string &bin)
{
    string res = bin;

    for (char &kt : res)
    {
        if (kt == '0')
            kt = '3';
        else
            kt = '5';
    }

    return res;
}


int main()
{
    int K = 0;
    cin >> K;

    int groupPower = getLog2(K + 1);

    int positionInGroup = K - ((1 << groupPower) - 1);

    string resBin = bitset<32>(positionInGroup).to_string();
    resBin = resBin.substr(resBin.size() - groupPower);

    string res = getResult(resBin);

    cout << res << endl;
    return 0;
}
