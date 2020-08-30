function get_average($a) {
  $sum = 0; 
  for ($i = 0; $i < count($a); $i++){
    $sum = $sum + $a[$i];
  }
  return floor($sum/count($a));
}