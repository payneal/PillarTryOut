var chai = require('chai');
var expect = chai.expect ; 
var CategorizeNewMembers = require('../categorize-new-members');

describe('CategorizeNewMembers', function() {
    it('openOrSenior(data) should return a list of string values stating whether the respective member is to be placed in the senior or open category', function() { 
        var categorizeNewMembers = new CategorizeNewMembers();
        var ageHandicap = [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]];
        var expectedCategories = ["Open", "Open", "Senior", "Open", "Open", "Senior"]; 
        expect(categorizeNewMembers.openOrSenior(ageHandicap)).to.eql(expectedCategories);
    });
});
