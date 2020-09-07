function splitByValue(k, elements){
    let  returnArr = []; 
    for(i = 0; i < elements.length;i++){
      if(elements[i] < k){
        returnArr.push(elements[i]);
      }
    }
    for(i = 0; i < elements.length;i++){
      if(elements[i] >= k){
        returnArr.push(elements[i]);
      }
    }
    return returnArr;
  }