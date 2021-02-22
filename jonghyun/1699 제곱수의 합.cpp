#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int dp(vector<int>& seq, int n) {
   if (seq[n] != 0) {
   }
   else if (n <= 3) {
      seq[n] = n;
   }
   else {
      //n==12 : 2^3 + 2^2
      int closest = static_cast<int>(sqrt(n));
      int min = 100001;

      for (int i = closest; 1 <= i; i--) {
         int result = dp(seq, n - i * i) + 1;
         if (result < min) {
            min = result;
         }
      }
      seq[n] = min;
   }
   return seq[n];
}

int main() {
   int n;
   cin >> n;

   vector<int> seq(n + 1, 0);

   for (int i = 0; i <= n; i++) {
      dp(seq, i);
   }

   //for (auto& i : seq) {
   //   cout << i << " ";
   //}
   //cout << "\n";
   cout << seq[n] << "\n";

   return 0;
}
