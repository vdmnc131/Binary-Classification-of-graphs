#include <bits/stdc++.h>
using namespace std;

unordered_map<string, int> elements;

unordered_set<int> active, inactive;

int getInt(string d){
	int x = 0;
	for(char s : d){
		x*=10;
		x += s-'0';
	}
	return x;
}

int getLines(){
	ifstream fil;
	fil.open("number_ids.txt");
	string d;
	fil>>d;
	fil.close();
	return getInt(d);
}

void createIDs(){
	ifstream fil;
	fil.open("elements.txt");
	int lines;
	fil>>lines;
	for(int i = 0; i<lines; i++){
		string name; int id;
		fil>>name>>id;
		elements[name] = id;
	}
}

void createActive(){
	ifstream fil;
	fil.open("parsed_active.txt");
	int lines;
	fil>>lines;
	for(int i  = 0; i<lines; i++){
		int temp; fil>>temp;
		active.insert(temp);
	}
}

void createInActive(){
	ifstream fil;
	fil.open("parsed_inactive.txt");
	int lines;
	fil>>lines;
	for(int i  = 0; i<lines; i++){
		int temp; fil>>temp;
		inactive.insert(temp);
	}
}

int main(){
	int num_ids = getLines();
	createIDs();
	createActive();
	createInActive();
	int count = 0;
	unordered_map<int, int> ids;
	for(int ii = 0; ii<num_ids; ii++){
		string s;
		char kk;
		cin>>kk;
		cin>>s;
		int k = getInt(s);
		bool print = true;
		if(inactive.find(k) == inactive.end()){
			print = false;
		}
		if(print){
			ids[count] = k;
			cout<<"t "<<kk<<" ";
			cout<<count;
			cout<<endl;
		}
		int num_nodes;
		cin>>num_nodes;
		for(int i = 0; i<num_nodes; i++){
			string node;
			cin>>node;
			if(print) cout<<"v "<<i<<" "<<elements[node]<<endl;
		}
		int num_edges;
		cin>>num_edges;
		for(int i = 0; i<num_edges; i++){
			int p, q, l;
			cin>>p>>q>>l;
			if(print) cout<<"e "<<p<<" "<<q<<" "<<l<<"\n";
		}
		if(print) count++;
	}
	ofstream fil;
	fil.open("inactive_ids.txt");
	for(auto id : ids){
		fil << id.first << " " << id.second << endl;
	}
	fil.close();
	return 0;
}