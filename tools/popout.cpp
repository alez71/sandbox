#include "iostream"

using namespace std;

const int ROWS = 6;
const int COLS = 7;
const char player1 = 'X';
const char player2 = 'O';
const char EMPTY = '.';
const string players = "XO";


void printboard(char board[ROWS][COLS]){
    for(int i=ROWS-1;i>=0;i--){
        for(int j=0;j<COLS;j++){
            cout << board[i][j] << ' ';
        }
        cout << '\n';
    }
    for(int i=0;i<COLS;i++){
        cout << i << ' ';
    }
    cout << '\n';
}

bool checkinput(char operation, int select, int lowest[ROWS], char board[][7], char currplayer){
    if(operation != 'D' && operation != 'P'){
        return false;
    }
    if(select < 0 || select > 6){
        return false;
    }
    if(operation == 'D'){
        if(lowest[select] == 7){
            return false;
        }
    }
    if(operation == 'P'){
        if(board[0][select] != currplayer){
            return false;
        }
    }

    return true;

}

void drop(char board[ROWS][COLS], int select, int lowest[], char currplayer){
    int low = lowest[select];
    board[low][select] = currplayer;
    lowest[select]++;
}

void popout(char board[ROWS][COLS], int select, int lowest[], char currplayer){
    int low = lowest[select];
    for(int i=0;i<low;i++){
        board[i][select] = board[i+1][select];
    }
    board[low][select] = 0;
    lowest[select]--;
}

bool checkhorizontal(char board[ROWS][COLS], char currentplayer){
    for(int j=0;j<6;j++){
        for(int i=0;i<4;i++){
            if(board[j][i] == currentplayer 
            && board[j][i+1] == currentplayer 
            && board[j][i+2] == currentplayer 
            && board[j][i+3] == currentplayer){
                return true;
            }
        }   
    }

    return false;
}

bool checkvertical(char board[ROWS][COLS], char currentplayer){
    for(int j=0;j<7;j++){
        for(int i=0;i<3;i++){
            if(board[i][j] == currentplayer 
            && board[i+1][j] == currentplayer 
            && board[i+2][j] == currentplayer 
            && board[i+3][j] == currentplayer){
                return true;
            }
        }   
    }

    return false;
}

bool checkdiagonal(char board[ROWS][COLS], char currentplayer){
    for(int i=0;i<3;i++){
        for(int j=0;j<4;j++){
            if(board[i][j] == currentplayer 
            && board[i+1][j+1] == currentplayer 
            && board[i+2][j+2] == currentplayer 
            && board[i+3][j+3] == currentplayer){
                return true;
            }
        }   
    }

    for(int i=0;i<3;i++){
        for(int j=3;j<7;j++){
            if(board[i][j] == currentplayer 
            && board[i+1][j-1] == currentplayer 
            && board[i+2][j-2] == currentplayer 
            && board[i+3][j-3] == currentplayer){
                return true;
            }
        }   
    }

    return false;
}



bool checkwin(char board[ROWS][COLS], char currplayer){
    bool hor = checkhorizontal(board, currplayer);
    bool ver = checkvertical(board, currplayer);
    bool dia = checkdiagonal(board, currplayer);
    if(hor || ver || dia){
        return true;
    }else{
        return false;
    }
}

int updateboard(char board[ROWS][COLS], char operation, int select, int lowest[], char currplayer){
    if(operation == 'D'){
        drop(board, select, lowest, currplayer);
    }else if(operation == 'P'){
        popout(board, select, lowest, currplayer);
    }
    
    bool p1win = checkwin(board, player1);
    bool p2win = checkwin(board, player2);
    if(p1win && p2win){
        return 0;
    }else if(p1win && !p2win){
        return 1;
    }else if(!p1win && p2win){
        return 2;
    }else{
        return -1;
    }
}


bool checkdraw(char board[ROWS][COLS], char currplayer){
    bool haveempty = false;
    bool canpop = false;
    for(int j=0;j<COLS;j++){
        if(board[0][j] == currplayer){
            canpop = true;
        }
    }

    for(int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++){
            if(board[i][j] == EMPTY){
                haveempty = true;
            }
        }
    }

    if(canpop || haveempty){
        return false;
    }else{
        return true;
    }
}

int main(){
    char board[ROWS][COLS] = {EMPTY};

    int round = 0;

    for(int i=ROWS-1;i>=0;i--){
        for(int j=0;j<COLS;j++){
            board[i][j] = EMPTY;
        }
    }

    int lowest[ROWS+1] = {0};
    char currplayer = player1;
    char op;
    int select;

    printboard(board);

    while(true){

        cout << "Player " << currplayer << " moves: ";

        while(true){
            cin >> op >> select;
            if(checkinput(op, select, lowest, board, currplayer)){
                break;
            }else{
                cout << "Invalid move. Try again!\n";
                cout << "Player " << currplayer << " moves: ";
            }
        }

        int win = updateboard(board, op, select, lowest, currplayer);

        printboard(board);

        if(checkdraw(board, currplayer)){
            cout << "Draw game!";
            break;
        }

        if(win == 1){
            cout << "Player X wins!";
            break;
        }else if(win == 2){
            cout << "Player O wins!";
            break;
        }else if(win == 0){
            cout << "Draw game!";
            break;
        }

        round++;
        currplayer = players[round&1];

    }
}