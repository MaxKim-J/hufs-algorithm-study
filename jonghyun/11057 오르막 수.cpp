#include <iostream>
#include <vector>
#include <array>

using namespace std;

int dp(vector<array<int ,10>> &save, int n, int dec){
	if(save[n][dec]!=0){
		return save[n][dec];
	}
	
	if(n==0){
		save[n][dec]=1;
	}
	else{
		int sum=0;
		for(int i=0;i<=dec;i++){
			sum+=dp(save, n-1, i);
			sum%=10007;
		}
		save[n][dec]=sum;
	}
	
	return save[n][dec];
}

int main(){
	int n;
	cin>>n;
	
	array<int, 10> row={0};
	vector<array<int, 10>> save(n,row);
	
	int result_sum=0;
	for(int i=0;i<10;i++){
		result_sum+=dp(save, n-1, i);
	}
	
	cout<<result_sum%10007<<"\n";
	return 0;
}