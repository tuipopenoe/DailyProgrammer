// C++ 11.0
// Tui Popenoe
// Challenge139E.cpp - Pangrams

# include <iostream>
# include <string>
# include <utility>

bool pangram(string, string);

int main(){

    std::string alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l',
                       'm','n','o','p','q','r','s','t','u','v','w','x','y','z'}


    return 0;
}

bool pangram(string input, string alphabet){

    std::transform(input.begin(), input.end(), input.begin(), ::tolower);
    for(int i = 0; i < input.length() -1; i++){
        for(int j = 0; j < language.length() -1; j++){
            if(input[i] == language[j]){
                
            }
        }
    }
}