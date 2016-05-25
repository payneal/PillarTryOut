var assert = require('assert');
var SlidingSquareGame = require('../slidingSquare.js');

describe('Sliding Square Game', function (){
    describe('Module SlidingSquare', function (){
        it('should have slidingSquareGame Object',  function (){
            assert.equal(typeof SlidingSquareGame, 'object');
        });
        it('should have a way to set the amount of cols and rows',  function (){
            assert.equal(typeof SlidingSquareGame.setRowAndCol, 'function');
        });
        it('should have a function that sets up square before randomizing', function (){
            assert.equal(typeof SlidingSquareGame.initiallySetSquare, 'function');
        });
        it('should have a function that can display the board', function (){
            assert.equal(typeof SlidingSquareGame.getBoard, 'function');
        });
        it('should have a function that sets the answer', function (){
            assert.equal(typeof SlidingSquareGame.answer, 'function');
        });
        it('should have a function that checks if game is over', function (){
            assert.equal(typeof SlidingSquareGame.gameOver, 'function');
        });
        it('should have a function that moves puzzle', function (){
            assert.equal(typeof SlidingSquareGame.move, 'function');
        });
        it('should have a function that starts game with zipScene API', function (){
            assert.equal(typeof SlidingSquareGame.startZipGame, 'function');
        });
    });
    describe('SlidngSquare given out errors when necessary', function (){
        it('should get an error message if anything less than 2 is set for row and col', function (){
            //https://nodejs.org/api/assert.html#assert_assert_throws_block_error_message
            error = SlidingSquareGame.setRowAndCol(1);
            assert.equal(error, "must have value >= 2");
        });
        it("should give error that row/col is not set", function (){
            error = SlidingSquareGame.initiallySetSquare();
            assert.equal(error,'col/row not set');
        });
        it('should give you an error if you go looking for answer before its avalible',function (){
            error = SlidingSquareGame.answer();
            assert.equal(error,"game board not yet built");
        });
        it('should give you an error if you try to move a number that doesnt exit in square',function (){
            SlidingSquareGame.setRowAndCol(2);
            SlidingSquareGame.initiallySetSquare();
            error = SlidingSquareGame.move(8);
            assert.equal(error,"number not in square");
        });
        it('should give you an error if you try to move number not touching _ (blank square)',function (){
            SlidingSquareGame.setRowAndCol(2);
            SlidingSquareGame.initiallySetSquare();
            board = SlidingSquareGame.getBoard().toString();
            answer = [[0,1],[ 2,'_']].toString();
            assert.equal(board, answer);      
            error = SlidingSquareGame.move(0);
            assert.equal(error,"Not movable");
        });
        it('should give you an error if you try insert non number to zipGame',function (){
            error = SlidingSquareGame.startZipGame('hi', 8);
            assert.equal(error,"Zip game requires a int for size and difficulty");
        });
    });
    describe('SlidngSquare functionality', function (){
        it("should be able to set how many rows and cols are in Square",  function (){
            SlidingSquareGame.setRowAndCol(2);
            answer = SlidingSquareGame.getRowandCol();
            assert.equal(answer, 2);
        });
        //here is where I startedclear
        it("should fill the board in order with empty spot last", function (){
            SlidingSquareGame.setRowAndCol(2);
            SlidingSquareGame.initiallySetSquare();
            gameBoard = SlidingSquareGame.getBoard().toString();
            answer = [[0,1],[2,'_']].toString();
            assert.equal(gameBoard, answer);
            BordAnswer = SlidingSquareGame.answer();
            assert.equal(BordAnswer, answer);
        });
        it("should fill the board in order with empty spot last Double Check more rows/cols", function (){
            SlidingSquareGame.setRowAndCol(3);
            SlidingSquareGame.initiallySetSquare();
            gameBoard = SlidingSquareGame.board.theBoard.toString();
            answer = [[0,1,2],[3,4,5],[6,7,'_']].toString();
            assert.equal(gameBoard, answer);
            BordAnswer = SlidingSquareGame.answer();
            assert.equal(BordAnswer, answer);
        });
        it("should be able to tell if puzzle is solved", function (){
            SlidingSquareGame.setRowAndCol(2);
            SlidingSquareGame.initiallySetSquare();
            //didnt randomize so game is technically over since puzzle is in order
            gameOver =  SlidingSquareGame.gameOver();
            assert.equal(gameOver, true);
        });
        it("win board should have all numbers in order", function (){
            SlidingSquareGame.setRowAndCol(2);
            SlidingSquareGame.initiallySetSquare();
            winBoard = SlidingSquareGame.answer().toString();
            answer = [[0,1],[ 2,'_']].toString();
            assert.equal(winBoard, answer);
        });
        it("should be able to move _ to the side", function (){
            SlidingSquareGame.setRowAndCol(2);
            SlidingSquareGame.initiallySetSquare();
            SlidingSquareGame.move(2);
            gameBoard = SlidingSquareGame.getBoard().toString();
            answer = [[0,1],['_',2]].toString();
            assert.equal(gameBoard, answer);
        });
        it("should be able to move _ to the up/down", function (){
            SlidingSquareGame.setRowAndCol(2);
            SlidingSquareGame.initiallySetSquare();
            SlidingSquareGame.move(1);
            gameBoard = SlidingSquareGame.getBoard().toString();
            answer = [[0,'_'],[ 2,1]].toString();
            assert.equal(gameBoard, answer);
        });
        it("should say puzzle not solved if we move once after initilization", function (){
            SlidingSquareGame.setRowAndCol(2);
            SlidingSquareGame.initiallySetSquare();
            SlidingSquareGame.move(2);
            gameBoard = SlidingSquareGame.getBoard().toString();
            winBoard = SlidingSquareGame.answer().toString();
            gameOver =  SlidingSquareGame.gameOver(); 
            assert.notEqual(gameBoard, winBoard);
            assert.equal(gameOver, false);
        });
        it("should be able to fill square How I want the square", function (){
            SlidingSquareGame.startPlanedGame(4, [[0,'_', 2, 3], [5,1,10,9], [4,7,6,8], [13,11,14,12]]);
            board = SlidingSquareGame.getBoard().toString();
            answer = [[0,'_', 2, 3], [5,1,10,9], [4,7,6,8], [13,11,14,12]].toString();
            assert.notEqual(board, answer);
        });
        it("should  be able to pull zipscene api to set up game board", function (){

            // dont understand how to pull
            /*

            this works but I have to use callbacks so basically call function within function
                dont understand the difference between this and promisses 
            

            var request = require('request');

            var foo = function (error, response, body) {
                if (error || response.statusCode !== 200) { 
                    return "didnt work"; 
                }
                console.log('body', body); 
                var foo = body; 
                console.log('foo', foo); 
                return body; 
            };

            */

            //gameBoard = SlidingSquareGame.startZipGame(2,8);
            // I didnt like how api gave 0 so I just added 1
            // gameBoard = SlidingSquareGame.getBoard().toString();
            // expected = [[1,2,3],['_', 5, 6], [4,7,8]].toString();
            //expectedURL = 'http://codetest.zipscene.com/puzzle?size=2&difficulty=8';
            //assert.equal(gameBoard, expectedURL);
            assert.equal("help", "need it"); 
        });
        it("should be able to post data to zipscene api to check solution", function (){
            
            // dont understand how this would work
            /*

            request.post(
                'http://codetest.zipscene.com/verify?size=3&id=xfzEgisOA5&difficulty=8',
                { form: {"id": "xfzEgis0A5", "body": "[[2,1],[2,2]]"} },
                function (error, response, body) {
                    if (!error && response.statusCode == 200) {
                        console.log(body)
                    }
                }
            );

            */
            assert.equal("help", "need it"); 
        });
    });
    describe('SlidngSquare walkthrough of easy example', function (){
        it("walk through http://codetest.zipscene.com/puzzle?size=3&difficulty=8 ", function (){
            SlidingSquareGame.startPlanedGame(3, [[0,1,'_'],[3,4,2],[6,7,5]]);
            gameOver = SlidingSquareGame.gameOver();
            assert.equal(gameOver, false);
            SlidingSquareGame.solve();
            steps = SlidingSquareGame.steps().toString();
            expectedAnswer = [ [ 2, 1 ], [ 2, 2 ] ].toString();
            assert.equal(steps, expectedAnswer);
            board = SlidingSquareGame.getBoard().toString();
            answer = SlidingSquareGame.answer().toString();
            assert.equal(board, answer);
            gameOver = SlidingSquareGame.gameOver();
            assert.equal(gameOver, true);
        });
         it("should be able to fill square How I want the square", function (){
            SlidingSquareGame.startPlanedGame(4, [[0,'_', 2, 3], [5,1,10,9], [4,7,6,8], [13,11,14,12]]);
            board = SlidingSquareGame.getBoard().toString();
            answer = [[0,'_', 2, 3], [5,1,10,9], [4,7,6,8], [13,11,14,12]].toString();
            assert.notEqual(board, answer);
        });

    });
});
