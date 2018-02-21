#include<stdio.h>
#include <stdlib.h>
#include<time.h>

int N,B,C,T;
main(){

srand(time(0));
FILE * file1 = fopen("2.txt", "r");
	FILE *f = fopen("output.txt", "w");
	if (f == NULL)
	{
    	printf("Error opening file!\n");
    	exit(1);
	}
	fscanf(file1,"%d\n%d\n%d\n%d\n",&T,&N,&B,&C);

float ts = (float)clock()/CLOCKS_PER_SEC;
	float te = 0, TimeInSec = 0;
	TimeInSec = T * 60.0;	
	float totalTime = 0;


int REV_TABLE[B][3];
int *BID_ARRAY[B];
int BID_NUMBER[B];
int BID_NUMBER1[B];
for (int r=0;r<B;r++){
BID_NUMBER[r]=0;
BID_NUMBER1[r]=0;
}
//int COMPANY[C]={0};

//Total no. of bids is B starting from 0 and each bid has variable length
int BID_COUNT=0;

for (int i=0;i<C;i++){            //for loop for all the companies
  int cid,ncid;
  fscanf(file1,"%d %d\n",&cid,&ncid);

  for(int j=0;j<ncid;j++){        //for loop for all the bids of that company
   int cid1,nbid,revenue;
    fscanf(file1,"\n%d %d %d ",&cid1,&nbid,&revenue);
    REV_TABLE[BID_COUNT][0]=cid1;
    REV_TABLE[BID_COUNT][1]=nbid;
    REV_TABLE[BID_COUNT][2]=revenue;
    //fprintf(f,"%d %d %d\n",cid1,nbid,revenue);
    
    BID_ARRAY[BID_COUNT]=(int *)malloc(nbid * sizeof(int)); //creating the array if Np_OF_bids size

    for(int k=0;k<nbid;k++){                 //scanning each bid blocks and marking them in the array
    fscanf(file1,"%d ",&BID_ARRAY[BID_COUNT][k]);
     }

   BID_COUNT++;
   }
  
}



//******************************************Input taking is completed************************



int CHILD[B][B];
for (int i=0;i<B;i++){
    int BLOCK[N];

    for(int l=0;l<N;l++){
       BLOCK[l]=0;
    }

    int c=REV_TABLE[i][1];
    
    for(int l=0;l<c;l++){
       int h=BID_ARRAY[i][l];
       BLOCK[h]=1;
    }   
     
    for(int j=0;j<B;j++){
       int c=REV_TABLE[j][1];
       int a=1;
       for(int l=0;l<c;l++){
       int h=BID_ARRAY[j][l];
         if(BLOCK[h]==1){
         a=0;
         break;  
         }
       } 
       //int d=REV_TABLE[j][0];  
       if(a==1 && REV_TABLE[i][0]!=REV_TABLE[j][0]){   
          CHILD[i][j]=1;
       }
       else{
          CHILD[i][j]=0;
       }


    }

}

//CHILD TABLE IS COMPLETED



int MAX_CHILD[B];
for(int i=0;i<B;i++){
int max=0;
MAX_CHILD[i]=-1;
int T=-1;

	for(int j=0;j<B;j++){
           if(CHILD[i][j]==1){
            int REVENUE=REV_TABLE[j][2];
              if(REVENUE>max){
               max=REVENUE;
               T=j;
               }
           }
        }
if(max>0){
MAX_CHILD[i]=T;
}


}




























//************************************************while loop starts from here
int max=0;
int X=0;
while(1){                        //This is for time constraint
/*if(p==10)
break;*/
//fprintf(f,"%d ",X++);
int K=0;
te = (float)clock()/CLOCKS_PER_SEC;
		totalTime = (te - ts);
		if( totalTime  > TimeInSec ){
			break;
		}
for (int r=0;r<B;r++){
BID_NUMBER[r]=0;
}

int BLOCK_TABLE[N];
int COMPANY[C];
srand(time(0));
int state=rand();
state=state%B;

for (int y=0;y<N;y++){
BLOCK_TABLE[y]=0;
}

int count,REVENUE;
count=REV_TABLE[state][1];
REVENUE=REV_TABLE[state][2];

for (int i=0;i<count;i++){             //marking the coal blocks
int U=BID_ARRAY[state][i];
BLOCK_TABLE[U]=1;
}

BID_NUMBER[state]=1;                   //marking the BIDNUMBER


for (int w=0;w<C;w++){
COMPANY[w]=0;
}
int f=REV_TABLE[state][0];
COMPANY[f]=1;                          //marking the company

int STATE=state;

int p=0;
int S=0;
	while(p!=(B*B)){
         int prob=rand();
         if(prob%2==0 && S==0){
         state=MAX_CHILD[STATE];
         S=1;
         }
         else{
          if(K!=B){
		  do{
		  state=rand();
		  state=state%B;
		  }while(CHILD[STATE][state]==0);
          }
         }
          int COM_ID,BLOCK_COUNT,REVENUE1;
          COM_ID=REV_TABLE[state][0];
          BLOCK_COUNT=REV_TABLE[state][1];
          REVENUE1=REV_TABLE[state][2];
          
          if(BID_NUMBER[state]==0){
          	
		if(COMPANY[COM_ID]==0){
			int check=1;
                   for(int s=0;s<BLOCK_COUNT;s++){
                     int l=BID_ARRAY[state][s];
                     if(BLOCK_TABLE[l]==1){
                         check=0;
                         break; 
                       }                   
                  
                    }
                   if(check==1){
                    REVENUE=REVENUE+REVENUE1;
                    for(int s=0;s<BLOCK_COUNT;s++){
                     int l=BID_ARRAY[state][s];
                     BLOCK_TABLE[l]=1;
                     }
                    COMPANY[COM_ID]=1;
                    BID_NUMBER[state]=1;
                    p=0;
                    STATE=state;
                    K=0;
                    S=0;
                   }
                   else{
                   K++;
                   }
                
                }

           
          }          
	
        
	p++;
	}          //end of while2

if(REVENUE>max){
max=REVENUE;
 for(int y=0;y<B;y++){
  BID_NUMBER1[y]=BID_NUMBER[y];
  }

}




} //end of while1

fprintf(f,"%d ", max);
for (int m=0;m<B;m++){
if(BID_NUMBER1[m]==1){
fprintf(f,"%d ",m);
}
}	


}
