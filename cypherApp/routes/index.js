var express = require('express');
var session = require('express-session');
var router = express.Router();

router.use(session({secret: 'keyword cat', resave: false, saveUninitialized: true, cookie: {maxAge:60000}}));



/* GET home page. */
router.get('/', function(req, res, next) {
  let inputAreaText = req.session.inputAreaText ||  "input your text here";
  let outputAreaText = req.session.outputAreaText || "output will display here";
  let key = req.session.key || "0";
  res.render('index', { inputAreaText: inputAreaText , outputAreaText: outputAreaText, key : key});
});


// router.get("/main", function(req, res, next) {
//   let inputAreaText = req.session.inputAreaText;
//   let outputAreaText = req.session.outputAreaText;
//   res.render('index', { inputAreaText: inputAreaText , outputAreaText: outputAreaText});
// });



module.exports = router;