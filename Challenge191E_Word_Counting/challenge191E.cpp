// Tui Popenoe
// challenge191E.cpp - Word Count

#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main(){
    string line;
    map<string, int> word_map;
    map<string, int>::iterator it;
    ifstream input_file("input.txt");
    if(input_file.is_open()){
        while(getline(input_file, line)){
            cout << line << '\n';
            word_map[line] += 1;
        }
        input_file.close();
    }
    for(it = word_map.begin(); it != word_map.end();){
        cout << it->first << ':' << it->second << endl;
    }

    return 0;
}