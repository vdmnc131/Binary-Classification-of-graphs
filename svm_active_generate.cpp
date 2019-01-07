#include <bits/stdc++.h>
using namespace std;

unordered_map<int, int> values;

int getLines(){
	ifstream fil;
	fil.open("num_lines_active.txt");
	int x;
	fil>>x;
	fil.close();
	return x;
}

void getIDs(){
	ifstream fil;
	fil = open();
	int num_ids;
	fil >> num_ids;
	for(int i = 0; i<num_ids; i++){
		int x, y;
		fil >> x >> y;
		values[x] = y;
	}
}

int main() {
	int num_lines;
	fil >> num_lines;
	for(int i = 0; i<num_lines; i++){
		char t;	cin>>t;
		char hash; cin>>hash;
		int id;	cin>>id;
		int count; cin>>count;
		char v;
		cin>>v;
		while(v - 'v' == 0){
			int id; cin >> id; cin >> id;
			cin>>v;
		}
		while(v - '\n' == 0){
			int id; cin>>id;
			mat[values[id]][count] = 1;
		}
	}
}