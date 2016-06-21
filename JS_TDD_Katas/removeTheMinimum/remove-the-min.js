"use strict";
function RemoveTheMin(){


    let _findLowestNumber = function(numbers){
        let lowest = numbers[0];
        let count = 0;
        let lowNumIndex = 0;
        for (let x of numbers){
            if (lowest > x ) {
                lowest = x; 
                lowNumIndex = count; 
            }            
            count = count + 1; 
        }
        return lowNumIndex;
    };
    
    this.remove_smallest = function(numbers) {     
        let lowNumIndex = _findLowestNumber(numbers);
        numbers.splice(lowNumIndex,1);
        return numbers;
    };
}
module.exports = RemoveTheMin;
