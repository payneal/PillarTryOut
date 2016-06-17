"use strict";
function CategorizeNewMembers() {
    //private
    let _isSeniorOrOpen = function(info,playerCats){
        if (info[0] >= 55 && info[1] >7){
                playerCats.push("Senior");    
            }else {
                playerCats.push('Open');
            } 
    };

    //public
    this.openOrSenior = function(data) {
        let playerCategories = [];
        for (let x of data){
            _isSeniorOrOpen(x, playerCategories);
        } 
        return playerCategories;
    };
}
module.exports = CategorizeNewMembers;
