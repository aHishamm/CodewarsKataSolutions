def expression_out(exp):
    operatorDict = { '+':   'Plus ',
  '-':   'Minus ',
  '*':   'Times ',
  '/':   'Divided By ',  
  '**':  'To The Power Of ',
  '=':   'Equals ',
  '!=':  'Does Not Equal ' }
    numberDict = { '1': 'One', '2': 'Two', '3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten'}
    exp = exp.split(' ')
    if exp[1] not in operatorDict.keys(): 
        return 'That\'s not an operator!'
    print(numberDict.get(exp[0])+' '+operatorDict.get(exp[1])+numberDict.get(exp[2]))
    return numberDict.get(exp[0])+' '+operatorDict.get(exp[1])+numberDict.get(exp[2])