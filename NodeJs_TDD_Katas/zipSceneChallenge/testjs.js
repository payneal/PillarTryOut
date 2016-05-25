// this is an example of callbacks I think .....



test  = {}

test.addOne = function(one) {
 return 1;  
};  
test.addTwo = function(one,two) {
  one += two(); 
  return one; 
}; 
test.addThree= function(one, two, three) {
 var x = one();
 x = two(x, one)
 x += three; 
 return x; 
}; 


var h = test.addThree(test.addOne, test.addTwo, 2); 
console.log(h)



