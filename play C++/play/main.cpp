#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;



void BFS(string s, map<string, vector<string>> graph, map<string, int> levels ){
    levels[s] = 0;
    
}



int main(){
    cout << "HELLO" << endl;
    map<string, int> levels;
    map <string, vector<string>> graph;
    string stuff[] = {"A", "B", "C"};
    cout << boolalpha << levels.empty() << endl;
//    levels["ANY"] = 2;
    if (levels.find("ANY") == levels.end()){
        cout << "YEah "  << endl;
    }
}
