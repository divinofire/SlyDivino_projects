var express = require('express');
var session = require('express-session');
var router = express.Router();
var fileupload = require("express-fileupload");
var bodyParser = require("body-parser");
var cypher = require("../scripts/cypher");


router.use(session({secret: 'keyword cat',  resave: false, saveUninitialized: true, cookie: {maxAge:60000}}));

//******************* file upload *********************************//

router.use(fileupload());
router.use(bodyParser.urlencoded({extended: false}));

router.post('/loadfile', (req, res) => {
  console.log("react to post action - loadFile");
  
  try{
      var logFile = req.files.fileName;
      var inputAreaText = req.body.inputText;
      var outputAreaText = req.body.outputText;

      var key = req.body.key;
      var keyChanged = false;
      if (key=='') key = 0;
      else {
        key = Number(key);
        key = parseInt(key);
      }
      let encrypt = req.body['encrypt'];
      if (encrypt == "false"){ key = -key; keyChanged=true;};
      console.log(req.body);
      let buffer = logFile.data;
      let myData = buffer.toString('utf8');
      var linesOfData = myData.split("\n");
      console.log("this is the text input \n");
      console.log(myData);
}

catch(error){

  key = 0;
  linesOfData = [" ## ENCRYPTION OR DECRYPTION PROCESS FAILED!","#### You must be kidding me, you haven't choosen a valid file. ####"]
}
  //cypher of data
  console.log("\n\nthis is the output text");
  let cyphered = "";
  linesOfData.map((line)=>{
    cyphered += cypher(line, key) + "\n"; 
  });

  outputAreaText = cyphered;

  req.session.inputAreaText = inputAreaText;
  req.session.outputAreaText = outputAreaText;
  if (keyChanged) key = -key;
  req.session.key = key;


  res.redirect("..");
console.log(cyphered);



// decyphered text
//var decyphered = "";
console.log("\n\nthis is the input text again");
cyphered.split("\n").map((line)=>console.log(cypher(line, -key)));
    

});

//************************* text upload **************************************//

router.post('/loadtext', (req, res) => {
  
  console.log("react to post action - loadtext");
  
 var inputAreaText = req.body.inputText;
  var outputAreaText = req.body.outputText;
  //res.redirect("..");
  // Notice the addition of the "fileName" key
  // It is the HTML name attribute value here in the input element:
  // <td><input type="file" name="fileName"></td>
  let myData = req.body.inputText;
  let key = req.body.key;
  let keyChanged = false;
  if (key=='') key = 0;
  else {
    key = Number(key);
    key = parseInt(key);
  }
  let encrypt = req.body['encrypt'];
  if (encrypt == "false"){ key = -key; keyChanged = true;};
  // console.log(req.body);
  // let buffer = logFile.data;
  // let myData = buffer.toString('utf8');
  let linesOfData = myData.split("\n");
  console.log("this is the text input \n");
  console.log(myData);

  //cypher of data
  console.log("\n\nthis is the output text");
  
  let cyphered = "";
  linesOfData.map((line)=>{
    cyphered += cypher(line, key) + "\n"; 
  });
outputAreaText = cyphered;

req.session.inputAreaText = inputAreaText;
req.session.outputAreaText = outputAreaText;
if (keyChanged) key = -key;
req.session.key = key;
//res.redirect("/main");
res.redirect("..");
console.log(cyphered);

// decyphered text
console.log("\n\nthis is the input text again");
cyphered.split("\n").map((line)=>console.log(cypher(line, -key)));
    

});



module.exports = router;
