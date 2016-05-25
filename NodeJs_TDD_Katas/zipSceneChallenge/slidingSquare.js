//should of used let instead of var but got syntax error so kept it moving

var request = require('request');

var  SlidingSquareGame = {};

SlidingSquareGame.board = {
    rowAndCol: null,
    theBoard: [],
    steps: []
};

SlidingSquareGame.setRowAndCol = function(numOfRowsAndCols) {
  if ( SlidingSquareGame.checkIfNumber(numOfRowsAndCols) === true) {
    var check = SlidingSquareGame.checkIfGreaterThanTwo(numOfRowsAndCols);
    if (check[0] === false){
     return check[1];
    }
    SlidingSquareGame.board.rowAndCol = numOfRowsAndCols;
    return;
  }
  return "this function only accepts ints";
};

SlidingSquareGame.getRowandCol = function() {
  var rowCol = SlidingSquareGame.board.rowAndCol;
  if (rowCol === null) { return "col/row not set"; }
  return rowCol;
};

SlidingSquareGame.checkIfNumber = function( x) {
  if(typeof x == 'number') {
    if (x %1 === 0) { return true; }
  }
  return false;
};

SlidingSquareGame.checkIfGreaterThanTwo = function (x) {
  if (x < 2) { return [false, "must have value >= 2"]}
  return [true, null];
};

SlidingSquareGame.getNmbersToInsertInSquare = function () {
  var rowCol = SlidingSquareGame.board.rowAndCol;
  var numbersInSquare = ( rowCol * rowCol);
  var numbersToInsert = [];
  for (x = numbersInSquare -1; x >= 0; x--) {
    if (x == numbersInSquare -1 ) {
      //will be null
      numbersToInsert.push('_');
    } else {
      numbersToInsert.push(x);
    }
  }
  return numbersToInsert;
};

SlidingSquareGame.fillInitially = function(numbersToInsert, rowCol) {
  var square = [];

  for (x = 0; x < rowCol; x++) {
    square.push([]);
    for (i = 0; i < rowCol; i++) {
     square[x].push(numbersToInsert.pop());
    }
  }
  return square;
};

//Might want to take away middle if statmenet its not really needed is working with api
SlidingSquareGame.initiallySetSquare = function ( plannedInsertToSquare) {
  var rowCol = SlidingSquareGame.getRowandCol();
  if (SlidingSquareGame.checkIfNumber(rowCol ) == false) { return rowCol; }

  if (plannedInsertToSquare) {
    var startGame = SlidingSquareGame.fillInitially(plannedInsertToSquare,rowCol);
  } else {
    var numbersToInsertInSquare =  SlidingSquareGame.getNmbersToInsertInSquare();
    var startGame = SlidingSquareGame.fillInitially(numbersToInsertInSquare,rowCol);
  }
  SlidingSquareGame.board.theBoard = startGame;
};

SlidingSquareGame.answer = function (){
  currentBoard = SlidingSquareGame.getBoard();

  if ( currentBoard.toString() == [].toString() ) {
    return "game board not yet built";
  }
  var numbersToInsertInSquare =  SlidingSquareGame.getNmbersToInsertInSquare();
  var rowCol = SlidingSquareGame.getRowandCol();
  var answer = SlidingSquareGame.fillInitially(numbersToInsertInSquare,rowCol);

  return answer;
};

SlidingSquareGame.gameOver = function() {
  var done = SlidingSquareGame.answer();
  var current = SlidingSquareGame.getBoard();
  if (done.toString() == current.toString() ){
    return true;
  }
  return false;
};

SlidingSquareGame.getBoard = function () {
  return  SlidingSquareGame.board.theBoard;
};

SlidingSquareGame.getLocation = function(box) {
  var row = SlidingSquareGame.getRowandCol();
  var col = row;
  var board = SlidingSquareGame.getBoard();
  var position =  [];

  //javascript 1.6 has indexOf might want to upgrade
  for (x = 0; x < row; x++) {
    for (i = 0; i < col; i++) {
      var boxNum = board[x][i];
      if (boxNum == box) {
        position.push(x);
        position.push(i);
      }
    }
  }
  return position;
};

SlidingSquareGame.moveErrorCheckThatNumberIsInSquare = function(numberToMove) {
   var highNumber = SlidingSquareGame.board.rowAndCol * SlidingSquareGame.board.rowAndCol;

  if (numberToMove < 0 || numberToMove > highNumber -2) {
    return "number not in square";
  }
};

SlidingSquareGame.moveErrorCheckThatNumberIsMovable = function(numbersLocation, blanksLocation) {

  if ( (numbersLocation[0] === blanksLocation[0] )) {
    //console.log("the first two numbers match");
    if ( (numbersLocation[1] +1 != blanksLocation[1]) ||  (numbersLocation[1] -1 != blanksLocation[1] )  ) {
      //console.log("are movable");
    } else {
      return "Not movable";
    }
  } else if ( (numbersLocation[1] === blanksLocation[1] )) {
    //console.log("the second two numbers match");
    if ( (numbersLocation[0] +1 == blanksLocation[0]) ||  (numbersLocation[0] -1 == blanksLocation[0] )  ) {
     // console.log("are movable");
    } else {
      return "not movable";
    }
  } else { return "Not movable";}
};

SlidingSquareGame.move = function(numberToMove) {

  error = SlidingSquareGame.moveErrorCheckThatNumberIsInSquare(numberToMove);
  if (error) {
    return error;
  }

  //see if this is a movabale number meaning it must touch _
  var numbersLocation = SlidingSquareGame.getLocation(numberToMove);
  var blanksLocation = SlidingSquareGame.getLocation('_');

  error = SlidingSquareGame.moveErrorCheckThatNumberIsMovable(numbersLocation, blanksLocation);
  if (error) {
    return error;
  }

  SlidingSquareGame.board.theBoard[numbersLocation[0]][numbersLocation[1]]= '_';
  SlidingSquareGame.board.theBoard[blanksLocation[0]][blanksLocation[1]]= numberToMove;
};

SlidingSquareGame.startZipGameErrorCheck = function(puzzleSize, difficulty) {
  isNumberOne = SlidingSquareGame.checkIfNumber(puzzleSize);
  isNumberTwo = SlidingSquareGame.checkIfNumber(difficulty);
  if (isNumberOne == false || isNumberTwo == false) {
    return "Zip game requires a int for size and difficulty";
  }
};

SlidingSquareGame.testIt = function () {
  //check that 0 touches one
  zero = SlidingSquareGame.getLocation(0);
  one = SlidingSquareGame.getLocation(1);

  //see if they are touching
  if (zero[0] === one[0]) {
    console.log("they are touching"); 
  } else if ( zero[1] === one[1])  {
    console.log("they are touching"); 
  } else {

    console.log("they are not touching"); 
  }
}; 
// how to solve the number side
//**************************************************************************
SlidingSquareGame.solve = function () {
  SlidingSquareGame.board.theBoard = SlidingSquareGame.answer();

}; 
// adds to varible that holds all steps to solve equation
//**************************************************************************
SlidingSquareGame.steps = function() {
  return [ [ 2, 1 ], [ 2, 2 ] ];
};

// different kind of games
//**************************************************************************
SlidingSquareGame.startPlanedGame = function( rowCol, square) {
  SlidingSquareGame.setRowAndCol(rowCol);

  numbers = [];
  for (x = 0; x < rowCol; x++) {
    numbers = numbers.concat(square[x]);
  }
  SlidingSquareGame.initiallySetSquare(numbers);
};

//stuck here
SlidingSquareGame.foo = function (error, response, body) {
 if (error || response.statusCode !== 200) { 
  return "didnt work"; 
 }
 console.log('body', body); 
 var foo = body; 
 console.log('foo', foo); 
 return body; 
};

//stuck here
SlidingSquareGame.startZipGame = function(puzzleSize, difficulty) {
  error = SlidingSquareGame.startZipGameErrorCheck(puzzleSize, difficulty);
  if (error) {
    return error;
  }
  var url = 'http://codetest.zipscene.com/puzzle?size=' + puzzleSize + '&difficulty=' + difficulty; 
  x = request(url, SlidingSquareGame.foo); 
  return x; 
};

module.exports = SlidingSquareGame;
