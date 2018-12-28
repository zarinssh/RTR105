#include <iostream>
#include <string>

using namespace std;
    bool findHorizontalyRight(string name, char letters[11][13], int x, int y);
    bool findHorizontalyLeft(string name, char letters[11][13], int x, int y);
    bool findVerticalyDown(string name, char letters[11][13], int x, int y);
    bool findVerticalyUp(string name, char letters[11][13], int x, int y);


int main() {
    string currentName;
    bool found;
    int startCoord[2] = {};
    int endCoord[2] = {};

    char letters[11][13] = {{'A', 'K', 'L', 'I', 'M', 'P', 'E', 'A', 'E', 'Z', 'B', 'W', 'M'},
                            {'K', 'A', 'E', 'N', 'Z', 'O', 'A', 'M', 'J', 'C', 'I', 'K', 'S'},
                            {'H', 'I', 'J', 'U', 'K', 'V', 'I', 'R', 'U', 'S', 'S', 'E', 'G'},
                            {'A', 'N', 'U', 'Z', 'M', 'Z', 'T', 'M', 'O', 'B', 'S', 'P', 'O'},
                            {'K', 'V', 'P', 'E', 'R', 'O', 'O', 'L', 'S', 'L', 'R', 'R', 'L'},
                            {'E', 'I', 'L', 'V', 'C', 'N', 'N', 'I', 'E', 'T', 'E', 'I', 'B'},
                            {'R', 'N', 'A', 'D', 'I', 'F', 'S', 'I', 'J', 'V', 'B', 'N', 'S'},
                            {'I', 'S', 'D', 'A', 'T', 'I', 'A', 'B', 'T', 'I', 'U', 'T', 'E'},
                            {'S', 'I', 'E', 'K', 'L', 'R', 'T', 'A', 'P', 'O', 'G', 'E', 'N'},
                            {'I', 'R', 'T', 'S', 'M', 'A', 'J', 'A', 'Z', 'P', 'R', 'T', 'F'},
                            {'M', 'Z', 'I', 'B', 'A', 'T', 'M', 'I', 'N', 'A', 'D', 'S', 'S'}};

    string words[5] = {"ZIBATMINA","VIRUSS","DATI","BLOGS","HAKERIS"};

    for (int x = 0; x < 5; x++){
        currentName = words[x];
        for (int i = 0; i < 11; i++){
            for(int a = 0; a < 13; a++){
                if(currentName[0] == letters[i][a]){
                    found = findHorizontalyRight(currentName, letters, i, a);
                    if(found) {
                        startCoord[0] = i;
                        startCoord[1] = a;
                        endCoord[0] = i;
                        endCoord[1] = a + currentName.length() - 1;
                        cout << currentName << " koordinates ir (" << startCoord[0] << ", " << startCoord[1] << "), ("<< endCoord[0] << ", " << endCoord[1] << ")" << endl;
                    }
                    found = findHorizontalyLeft(currentName, letters, i, a);
                    if(found) {
                        startCoord[0] = i;
                        startCoord[1] = a;
                        endCoord[0] = i;
                        endCoord[1] = a - currentName.length() + 1;
                        cout << currentName << " koordinates ir (" << startCoord[0] << ", " << startCoord[1] << "), ("<< endCoord[0] << ", " << endCoord[1] << ")" << endl;
                    }
                else {
                    found = findVerticalyDown(currentName, letters, i, a);
                    if(found) {
                        startCoord[0] = i;
                        startCoord[1] = a;
                        endCoord[0] = i + currentName.length() - 1;
                        endCoord[1] = a;
                        cout << currentName << " koordinates ir (" << startCoord[0] << ", " << startCoord[1] << "), ("<< endCoord[0] << ", " << endCoord[1] << ")" << endl;
                    }
                    found = findVerticalyUp(currentName, letters, i, a);
                    if(found) {
                        startCoord[0] = i;
                        startCoord[1] = a;
                        endCoord[0] = i - currentName.length() + 1;
                        endCoord[1] = a;
                        cout << currentName << " koordinates ir (" << startCoord[0] << ", " << startCoord[1] << "), ("<< endCoord[0] << ", " << endCoord[1] << ")" << endl;
                    }
                }

                }

            }
        }
    }

    return 0;
}

bool findHorizontalyRight(string name, char letters[11][13], int x, int y) {
    bool foundName = true;
    if(name.length() <= 13 - y){
        for (int i = y; i < y + name.length(); i++) {
            if(name[i-y] != letters[x][i]) {
                foundName = false;
                break;
            }
        }
        if(foundName){
            return true;
        }
        else return false;
    }
    else{
        return false;
    }
}

bool findVerticalyDown(string name, char letters[11][13], int x, int y) {
    bool foundName = true;
    if(name.length() <= 11 - x){
        for (int i = x; i < x + name.length(); i++) {
            if(name[i-x] != letters[i][y]) {
                foundName = false;
                break;
            }
        }
        if(foundName){
            return true;
        }
        else return false;
    }
    else{
        return false;
    }
}

bool findVerticalyUp(string name, char letters[11][13], int x, int y) {
    bool foundName = true;
    if(name.length() <= x){
        for (int i = x; i > x - name.length(); i--) {
            if(name[x-i] != letters[i][y]) {
                foundName = false;
                break;
            }
        }
        if(foundName){
            return true;
        }
        else return false;
    }
    else{
        return false;
    }
}

bool findHorizontalyLeft(string name, char letters[11][13], int x, int y) {
    bool foundName = true;
    if(name.length() <= y){
        for (int i = y; i > y - name.length(); i--) {
            if(name[y-1] != letters[x][i]) {
                foundName = false;
                break;
            }
        }
        if(foundName){
            return true;
        }
        else return false;
    }
    else{
        return false;
    }
}
