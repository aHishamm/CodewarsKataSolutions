function descendingOrder(n){
    let digits = (""+n).split("");
    numbers = Array.from(n.toString()).map(Number);
    numbers.sort(function(a, b){return b-a});
    newNumbers = numbers.join("");
    return parseInt(newNumbers);
  }