#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"

void clearstring(char* str, char f){
    str[0] = f;
    int i = 1;
    while(str[i] != 0){
        str[i++] = 0;
    }
}

void checkrepeat(char* s1,char* s2,char* s3){
    if(strstr(s1, s2) != NULL){
        clearstring(s2, s1[0]);
    }else if(strstr(s2, s1) != NULL){
        clearstring(s1, s2[0]);
    }
    if(strstr(s2, s3) != NULL){
        clearstring(s3, s2[0]);
    }else if(strstr(s3, s2) != NULL){
        clearstring(s2, s3[0]);
    }
    if(strstr(s1, s3) != NULL){
        clearstring(s3, s1[0]);
    }else if(strstr(s3, s1) != NULL){
        clearstring(s1, s3[0]);
    }
}

int min(int a,int b){
    if(a<b){return a;}else{return b;}
}

int compare(char* s1, int s1start,char* s2, int s2start, int lenght){
    for(int i=0;i<lenght;i++){
        if(s1[s1start+i] != s2[s2start+i]){
            // printf("comparecheck\n");
            return 0;
        }
    }
    // system("PAUSE");
    return 1;
}

int combine(char* result, char* s1,int l1, char* s2, int index){
    // system("pause");
    strcpy(result,s1);
    // system("pause");
    int i = 0;
    while(s2[index+i] != 0){
        result[l1+i] = s2[index+i];
        i++;
    }
}

int checkinclusive(char* s1, char* s2,int l1,int l2, char* result){
    int max = -1;
    //check suffix of s1 match prefix of s2
    //s1='='
    // s2'='=
    for(int i=1;i<=min(l1,l2);i++){
        if(compare(s1,l1-i,s2,0,i)){
            if(max<i){
                max = i;
                combine(result, s1, l1, s2, i);
            }
        }
    }
    for(int i=1;i<=min(l1,l2);i++){
        if(compare(s1,0,s2,l2-i,i)){
            if(max<i){
                max = i;
                combine(result, s2, l2, s1, i);
            }
        }
    }
    return max;
}

int printarray(char* str){
    int i=0;
    while(str[i] != 0){
        printf("%c ",str[i]);
        i++;
    }
    printf("\n");
}

int findlenght(char* arr){
    int i = 0;
    while(arr[i] != 0){i++;}
    return i;
}

int findstring(char** address,int l1, int l2,int l3, char* middle, char* final){
    // while will run 2 time
    //first to merge one pair
    //second to merge another
    int run = 3;
    //c1 c2 stores the target to combine
    int a1,a2;
    while(run > 1){
        int max = -1;
        char nocmiddle[300000];
        //iterate over 3 string address
        for(int i=0;i<run;i++){
            for(int j=i+1;j<run;j++){
                int temp = checkinclusive(address[i], address[j],findlenght(address[i]),findlenght(address[j]), middle);
                if(max<temp){
                    max = temp;
                    strcpy(nocmiddle, middle);
                    a1 = i;
                    a2 = j;
                }
            }
        }
        run--;
        if(max == -1){
            // system("PAUSE");
            combine(middle,address[0],findlenght(address[0]),address[run],0);
            strcpy(address[0],middle);
        }else{
            strcpy(address[a1], nocmiddle);
            strcpy(address[a2], address[run]);
        }
    }
}

int main(){
    char s1[100000] = {0};
    char s2[100000] = {0};
    char s3[100000] = {0};
    char middle[300000] = {0};
    char final[300000] = {0};
    fgets(s1, 1000000, stdin);
    fgets(s2, 1000000, stdin);
    fgets(s3, 1000000, stdin);

    int lens1 = 0;
    while(s1[lens1] != 10){lens1++;};
    s1[lens1] = 0;
    int lens2 = 0;
    while(s2[lens2] != 10){lens2++;};
    s2[lens2] = 0;
    int lens3 = 0;
    while(s3[lens3] != 10){lens3++;};
    s3[lens3] = 0;

    checkrepeat(s1,s2,s3);
    checkrepeat(s1,s2,s3);

    lens1 = findlenght(s1);
    lens2 = findlenght(s2);
    lens3 = findlenght(s3);

    char* straddress[3] = {s1, s2, s3};
    findstring(straddress,lens1,lens2,lens3,middle,final);
    strcpy(final, straddress[0]);
    int a = 0;
    while(final[a]!=0){
        // printf("%c ",final[a]);
        a++;
    }
    printf("%d",a);
    // system("pause");
}