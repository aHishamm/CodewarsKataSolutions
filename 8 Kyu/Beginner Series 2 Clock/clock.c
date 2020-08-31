int past(int h, int m, int s) {
  int hMill = h * 60 * 60 * 1000;
  int mMill = m * 60 * 1000; 
  int sMill = s * 1000; 
  return hMill + mMill + sMill;
    

}