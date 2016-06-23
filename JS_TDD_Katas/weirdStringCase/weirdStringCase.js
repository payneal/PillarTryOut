"use strict";

function WeirdStringCase(){
    this._string = null;
    this._caps = true;
    this._count = 0;
    this._capsCount = 0;

    this.toWeirdCase = function(string) {
        this._string = string.split('');
        _cycleThroughLettersToBeChanged.call(this);
        return this._string.join('');
    };

    let _cycleThroughLettersToBeChanged = function(){
        for (let letter of this._string) {
            _shouldLettersBeCapped.call(this, letter); 
            this._count++;
            this._capsCount++;
            _changeCapsOrNot.call(this);
        }
    };

    let _shouldLettersBeCapped = function(letter){ 
        if (this._caps === true && letter !== ' ') {
            this._string[this._count] = letter.toUpperCase();
            this._caps = false;
        } 
        if (letter == ' ') {
            this._capsCount = -1;
        }
    };

    let _changeCapsOrNot = function() {
        if (this._capsCount%2 === 0){
            this._caps = true;
        }
    };

}
module.exports = WeirdStringCase;
