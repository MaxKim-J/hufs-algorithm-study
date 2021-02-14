#include <iostream>
#include <vector>

using namespace std;

int dp(vector<int> &save, int n){
	if(save[n]!=0){
		return save[n];
	}
	
	if(n==1){
		save[n]=1;
	}
	else if(n==2){
		save[n]=3;
	}
	else{
		save[n]=(dp(save, n-1) + dp(save,n-2)*2)%10007;
	}
	return save[n];
}

int main(){
	int n;
	cin>>n;
	
	vector<int> save(n+1,0);
	
	cout<<dp(save, n);
}