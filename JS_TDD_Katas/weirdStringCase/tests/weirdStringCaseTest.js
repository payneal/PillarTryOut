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
        it('one letter(not capped) should just return same string(capped)',function(){
            let weirdString = new WeirdStringCase();
            expect(weirdString.toWeirdCase('i')).to.equal('I');
        });
        it('2 letters(capped, not) should just return same string',function(){
            let weirdString = new WeirdStringCase();
            expect(weirdString.toWeirdCase('It')).to.equal('It');
        });
        it('3 letters(capped, not, not ) should just return same string(capped, not, capped)',function(){
            let weirdString = new WeirdStringCase();
            expect(weirdString.toWeirdCase('Its')).to.equal('ItS');
        });
        it('is a => Is A',function(){
            let weirdString = new WeirdStringCase();
            expect(weirdString.toWeirdCase('is a')).to.equal('Is A');
        });
        it('This is a test => ThIs Is A Test',function(){
            let weirdString = new WeirdStringCase();
            expect(weirdString.toWeirdCase('This is a test')).to.equal('ThIs Is A TeSt');
        }); 
    });
});
