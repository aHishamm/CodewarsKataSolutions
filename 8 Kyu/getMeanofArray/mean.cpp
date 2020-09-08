int get_average(std::vector <int> marks)
{
  int sum = 0; 
  int length = marks.size();
  for(int i = 0; i < length; i++){
    sum = sum + marks[i];
  }
  return sum/length;
}