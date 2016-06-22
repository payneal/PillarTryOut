"use strict";
let chai = require('chai');
let expect = chai.expect;

let WeirdStringCase = require('../weirdStringCase');

describe("weird case string", function() {
    describe("toWeirdCase(string) should return same string" +
        " with every other char caped " , function() {
        it('one letter(capped) should just return same string',function(){
            let weirdString = new WeirdStringCase();
            expect(weirdString.toWeirdCase('I')).to.equal('I');
        });
    });
});
