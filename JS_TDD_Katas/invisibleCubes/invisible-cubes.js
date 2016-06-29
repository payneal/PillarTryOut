"use strict";
function InvisibleCubes(){
    this.notVisibleCubes = function(x) {
        var row = x -2; 
        if (row <= 0){return 0;}
        var inside = row * row; 
        return  row * inside; 
    };
}
module.exports = InvisibleCubes;
