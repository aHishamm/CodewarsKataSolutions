class TimeUtils {
  public static String convertTime(int n) {
    int day = n / (24 * 3600); 
    n = n % (24 * 3600); 
    int hour = n / 3600; 
    n %= 3600; 
    int minutes = n / 60 ; 
    n %= 60; 
    int seconds = n; 
    return day+" "+hour+" "+minutes+" "+seconds;
  } 
}