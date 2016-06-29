var chai = require('chai');
var expect = chai.expect ; 
var InvisibleCubes = require('../invisible-cubes');

describe('Invisible Cubes', function() {
    var invisibleCubes = new InvisibleCubes();
    it('entering 1 rows should return 0 not visible from outside', function(){
        var notVisible = invisibleCubes.notVisibleCubes(1); 
        expect(notVisible).to.eql(0);
    });
    it('entering 3 rows should return 1 not visible from outside', function(){
        var notVisible = invisibleCubes.notVisibleCubes(3); 
        expect(notVisible).to.eql(1);
    });
    it('entering 5 rows should return 1 not visible from outside', function(){
        var notVisible = invisibleCubes.notVisibleCubes(5); 
        expect(notVisible).to.eql(27);
    });
});
