const express = require('express');
const passport = require('passport');
const bcrypt = require('bcrypt');
const { isLoggedIn, isNotLoggedIn } = require('./middlewares');
const { User } = require('../models');

const router = express.Router();

router.post('/join', isNotLoggedIn, async (req, res, next) => {
  const { email, nick, password } = req.body;
  try {
    const exUser = await User.find({ where: { email } });
    if (exUser) {
      return res.redirect('/join?error=exist');
    }
    const hash = await bcrypt.hash(password, 12);
    await User.create({
      email,
      nick,
      password: hash,
    });
    return res.redirect('/');
  } catch (error) {
    console.error(error);
    return next(error);
  }
});

router.post('/login', isNotLoggedIn, (req, res, next) => {
  passport.authenticate('local', (authError, user, info) => {
    if (authError) {
      console.error(authError);
      return next(authError);
    }
    if (!user) {
      return res.redirect(`/?loginError=${info.message}`);
    }
    return req.login(user, (loginError) => {
      if (loginError) {
        console.error(loginError);
        return next(loginError);
      }
      return res.redirect('/');
    });
  })(req, res, next); // 미들웨어 내의 미들웨어에는 (req, res, next)를 붙입니다.
});

router.get('/logout', isLoggedIn, (req, res) => {
  req.logout();
  req.session.destroy();
  res.redirect('/');
});

router.get('/kakao', passport.authenticate('kakao'));

router.get('/kakao/callback', passport.authenticate('kakao', {
  failureRedirect: '/',
}), (req, res) => {
  res.redirect('/');
});

module.exports = router;
// const express = require('express');
// const passport = require('passport');
// const bcrypt = require('bcrypt');
// const { isLoggedIn, isNotLoggedIn } = require('./middlewares');
// const { User } = require('../models');
// const router = express.Router();

// router.post('/join', isNotLoggedIn, async (req, res, next) => {
//     const { email, nick, password } = req.body;
//     try {
//         const exUser = await User.findOne({ where: { email } });
//         if (exUser) {
//             req.flash('joinError','이미 가입된 이메일입니다.');
//             return res.redirect('/join');
//         }
//         const hash = await bcrypt.hash(password, 12);
//         await User.create({
//             email,
//             nick,
//             password: hash,
//         });
//         return res.redirect('/');
//     } catch (error) {
//         console.error(error);
//         return next(error);
//     }
// });

// router.post('/login', isNotLoggedIn, (req, res, next) => {
//     passport.authenticate('local', (authError, user, info) => {
//         if (authError) {
//             console.error(authError);
//             return next(authError);
//         }
//         if (!user) {
//             req.flash('loginError', info.message);
//             return res.redirect('/');
//         }
//         return req.login(user, (loginError) => {
//             if (loginError) {
//                 console.error(loginError);
//                 return next(loginError);
//             }
//         return res.redirect('/');
//         })
//     ;})(req, res, next); // 미들웨어 내의 미들웨어에는 (req, res, next)를 붙입니다. });
// });

// router.get('/logout', isLoggedIn, (req, res, next) => {
//     req.logout();
//     req.session.destroy();
//     res.redirect('/');  // npm i passport@0.5 해야 실행됨 ->  0.6에서는 코드가 아래같이 변경됨
// });
// passport@0.6
/*
router.get('/logout', isLoggedIn, (req, res) => {
  req.logout((err) => {
    if (err) { return next(err); }
    req.session.destroy();
    res.redirect('/');
  });
});
*/

// kakao login
router.get('/kakao', passport.authenticate('kakao'));
router.get('/kakao/callback', passport.authenticate('kakao', {
    failureRedirect: '/',
}), (req, res) => {
    res.redirect('/');
});

module.exports = router;