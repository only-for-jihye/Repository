const express = require('express');
const { v4: uuidv4 } = require('uuid');
const { User, Domain } = require('../models');
const { isLoggedIn } = require('./middlewares');

const router = express.Router();

router.get('/', async (req, res, next) => {
  try {
    const user = await User.findOne({
      where: { id: req.user && req.user.id || null },
      include: { model: Domain },
    });
    res.render('login', {
      user,
      domains: user && user.Domains,
    });
  } catch (err) {
    console.error(err);
    next(err);
  }
});

router.post('/domain', isLoggedIn, async (req, res, next) => {
  try {
    await Domain.create({
      UserId: req.user.id,
      host: req.body.host,
      type: req.body.type,
      clientSecret: uuidv4(),
    });
    res.redirect('/');
  } catch (err) {
    console.error(err);
    next(err);
  }
});

module.exports = router;
// const express = require('express');
// const uuidv4 = require('uuid/v4'); //uuid는 범용 고유 식별자(uni versally unique identifier)로 고유한 문자열을 만들고 싶을 때 사용합니다. 완 벽하게 고유하진 않지만 실제 사용 시 중복될 가능성은 거의 없습니다.
// const { User, Domain } = require('../models');
// const router = express.Router();

// router.get('/', (req, res, next) => {
//     User.findOne({
//         where: { id: req.user && req.user.id || null },
//         include: { model: Domain },
//     })
//     .then((user) => {
//         res.render('login', {
//             user,
//             loginError: req.flash('loginError'),
//             domains: user && user.domains,
//         }); 
//     })
//     .catch((error) => {
//         next(error);
//     }); 
// });

// router.post('/domain', (req, res, next) => {
//     Domain.create({
//         userId: req.user.id,
//         host: req.body.host,
//         type: req.body.type,
//         clientSecret: uuidv4(),
//     })
//     .then(() => {
//         res.redirect('/');
//     })
//     .catch((error) => {
//         next(error);
//     }); 
// });

// module.exports = router;