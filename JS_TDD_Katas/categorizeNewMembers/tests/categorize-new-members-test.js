var chai = require('chai');
var expect = chai.expect ; 
var CategorizeNewMembers = require('../categorize-new-members');

describe('CategorizeNewMembers', function() {
    describe('openOrSenior(data) should return a list of string values stating whether the respective member is to be placed in the senior or open category', function() { 
         it('case #1', function() {
            var categorizeNewMembers = new CategorizeNewMembers();
            var  ageHandicap = [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]];
            var expectedCategories = ["Open", "Open", "Senior", "Open", "Open", "Senior"]; 
            expect(categorizeNewMembers.
                openOrSenior(ageHandicap)).to.eql(expectedCategories);
         });
         it('case #2', function() {
            var categorizeNewMembers = new CategorizeNewMembers();
             var ageHandicap =[[45, 12],[55,21],[19, -2],[104, 20]]; 
             var expectedCategories = ['Open', 'Senior', 'Open', 'Senior'];
             expect(categorizeNewMembers.
                 openOrSenior( ageHandicap)).to.eql(expectedCategories);
        });
        it('case #3', function() {
            var categorizeNewMembers = new CategorizeNewMembers();
             var ageHandicap = [[59, 12],[55,-1],[12, -2],[12, 12]]; 
             var expectedCategories = ['Senior', 'Open', 'Open', 'Open']; 
             expect(categorizeNewMembers.
                 openOrSenior( ageHandicap)).to.eql(expectedCategories);
        });
    });
});
