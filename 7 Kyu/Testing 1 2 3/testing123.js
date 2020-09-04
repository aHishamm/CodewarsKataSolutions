let number=function(array){
    let returnArr = [] 
    for(i =0; i < array.length; i++){
      returnArr.push((i+1).toString()+": "+array[i]);
    }
    return returnArr;
  }