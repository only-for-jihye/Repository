var express = require('express');
var User = require('../models').User;
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  User.findAll()
   .then((users) => {
     res.render('sequelize', { users });
    })
   .catch((err) => {
    console.error(err);
    next(err);
   });
});
//   res.render('index', { title: 'Express' });
// });

module.exports = router;
