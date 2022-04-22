#include "iostream"
#include "algorithm"
#include "deque"
using namespace std;

const int NUMVERTEX = 16;

char inttochar(int num){
    return (char)num+65;
}

int checkline(int station){
    //stations of each line
    int green[] = {0,1,2,3};
    int yellow[] = {5,6,7};
    int blue[] = {4,8,12,13};
    int white[] = {9,10,11,14,15};

    if(find(begin(green), end(green), station) != end(green)){
        return 1;
    }
    if(find(begin(yellow), end(yellow), station) != end(yellow)){
        return 4;
    }
    if(find(begin(blue), end(blue), station) != end(blue)){
        return 2;
    }
    if(find(begin(white), end(white), station) != end(white)){
        return 3;
    }
    return -1;
}

bool isfalse(bool i){
    return !i;
}


void dijkstra(int graph[NUMVERTEX][NUMVERTEX], int src){
    //setting graph weight adjacent to src as 2 due to problem setting
    if(src+1 < 16 && src/4 == (src+1)/4){
        graph[src][src+1] = 2;
    }
    if(src-1 > -1 && src/4 == (src-1)/4){
        graph[src][src-1] = 2;
    }
    if(src+4 < 16){
        graph[src][src+4] = 2;
    }
    if(src-4 > -1){
        graph[src][src-4] = 2;
    }


    //set all distance to inf and src to 0
    int dist[NUMVERTEX];
    fill(dist, dist+NUMVERTEX, INT_MAX);
    dist[src] = 0;

    bool visited[NUMVERTEX] = {0};
    int previous[NUMVERTEX] = {0};
    previous[src] = src;

    while(find(begin(visited), end(visited), false) != end(visited)){
        //get current node and set visited
        int currnode, temp = INT_MAX;
        //get smallest unvisited element
        for(int i=0;i<NUMVERTEX;i++){
            if(dist[i] < temp && !visited[i]){
                currnode = i;
                temp = dist[i];
            }
        }

        //set current node to visited
        visited[currnode] = true;

        //update cost
        for(int i=0;i<NUMVERTEX;i++){
            //check if node is adjacent and distance is smaller
            if(graph[currnode][i] != INT_MAX && dist[currnode] + graph[currnode][i] < dist[i]){
                dist[i] = dist[currnode] + graph[currnode][i];
                previous[i] = currnode;
            }
        }
    }

    //print answer at end of function
    for(int i=0;i<NUMVERTEX;i++){
        cout << "Dist from " << inttochar(src) << " to " << inttochar(i) << " = " << dist[i] << "\n";
        cout << "Path = " << inttochar(i);
        int tempnode = previous[i];
        while(tempnode != src){
            cout << "<-" << inttochar(tempnode);
            tempnode = previous[tempnode];
        }
        cout << "<-" << inttochar(src) << "\n";
        cout << "-------------------------------------\n";
    }
}




int main(){

    //initize graph
    int graph[NUMVERTEX][NUMVERTEX];
    for(int i=0;i<NUMVERTEX;i++){
        for(int j=0;j<NUMVERTEX;j++){
            //check if equal to current node
            if(i-j == 0){
                graph[i][j] = 0;
                continue;
            }
            //check if next to current node
            if((j-i == 1 && j/4 == i/4)|| j-i == 4 || (j-i == -1 && j/4 == i/4) || j-i == -4){
                graph[i][j] = checkline(j);
                continue;
            }

            graph[i][j] = INT_MAX;
        }
    }



    dijkstra(graph, 12);

}