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

request('http://codetest.zipscene.com/puzzle?size=3&difficulty=8', foo);
//request('http://codetest.zipscene.com/puzzle?size=3&difficulty=8', foo);
//request('http://codetest.zipscene.com/puzzle?size=3&difficulty=8', foo);

//console.log('oh hai');


request.post(
    'http://codetest.zipscene.com/verify?size=3&id=xfzEgisOA5&difficulty=8',
    { form: {"id": "xfzEgis0A5", "body": "[[2,1],[2,2]]"} },
    function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body)
        }
    }
);