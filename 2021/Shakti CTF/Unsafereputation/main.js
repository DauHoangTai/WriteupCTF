var express = require('express');
var app = express();

app.get('/', function (req, res) {

  var inp = req.query.text;

  if(inp){
    const blacklist = ['system', 'child_process', 'exec', 'spawn', 'eval'];

    if(blacklist.map(v=>inp.includes(v)).filter(v=>v).length !== 0){
      res.send("That function is blocked, sorry XD");
      return;
    }

    res.send('Welcome to the world ' + eval(inp));
    console.log(req.query.text);
  }else{
    res.send("Hey aren't you missing something??");
    return;
  }
});

app.listen(4000, function () {
  console.log('app listening on port 4000!');
});

