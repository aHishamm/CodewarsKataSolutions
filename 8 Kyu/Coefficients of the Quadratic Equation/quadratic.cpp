#include <vector>
using namespace std;
vector<int> quadratic(int a,int b){
// Answer in vector
  vector<int> returnVec;
  int xqrt = 1 ; 
  int x = -b + -a; 
  int c = -a * -b; 
  returnVec = {xqrt,x,c};
  return returnVec;
  
}