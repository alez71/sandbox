#include "iostream"
#include "vector"
#include "utility"
using namespace std;

typedef struct{
    double centerx;
    double centery;
    int n;
    vector<pair<int ,int>> members;
}cluster;

int mandist(pair<int, int> target, cluster data){
    return abs(target.first - data.centerx) + abs(target.second - data.centery); 
}

int main(){
    vector<cluster> allcluster;
    vector<pair<int, int>> newpoint = {{0,0}, {0,0}, {1,2}, {3,5}};
    double theta = 1;
    for(auto &x : newpoint){
        if(allcluster.empty()){
            cluster temp = {.centerx = (double)x.first, .centery = (double)x.second, .n = 1, .members = {x}};
            allcluster.push_back(temp);
        }else{
            bool notfound = true;
            for(auto &a : allcluster){
                double dist = mandist(x, a);
                if(dist < theta){
                    a.members.push_back(x);
                    a.centerx = (a.centerx*a.n + x.first)/(a.n + 1);
                    a.centery = (a.centery*a.n + x.second)/(a.n + 1);
                    a.n++;
                    notfound = false;
                }
            }
            if(notfound){
                cluster temp = {.centerx = (double)x.first, .centery = (double)x.second, .n = 1, .members = {x}};
                allcluster.push_back(temp);
            }
        }
    }
    for(int i=0;i<allcluster.size();i++){
        cout << "Cluster " << i << " contains: ";
        for(pair x : allcluster.at(i).members){
            cout << "(" << x.first << "," << x.second << ") ";
        }
        cout << "\n";
    }
}