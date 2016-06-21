"use strict";
let chai = require('chai');
let expect = chai.expect;

let RemoveTheMin = require('../remove-the-min');

describe("remove the min", function() {
    describe('remove_smallest(arrayOfNums) should return the list without the smallest value in it', function() {
        it('case 1', function() {
            let removeTheMin = new RemoveTheMin();
            let numbers = [1,2,3,4,5];
            let expected = [2,3,4,5]; 
            expect(removeTheMin.remove_smallest(numbers)).to.deep.equal(expected);
        });
        it('case 2', function() {
            let removeTheMin = new RemoveTheMin();
            let numbers = [5,3,2,1,4];
            let expected = [5,3,2,4]; 
            expect(removeTheMin.remove_smallest(numbers)).to.deep.equal(expected);
        });
         it('case 3', function() {
            let removeTheMin = new RemoveTheMin();
            let numbers = [2,2,1,2,1];
            let expected = [2,2,2,1]; 
            expect(removeTheMin.remove_smallest(numbers)).to.deep.equal(expected);
        });



    });
});
