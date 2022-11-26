// 
const express = require('express');
const cookieParser = require('cookie-parser');
const morgan = require('morgan');
const path = require('path');
const session = require('express-session');
const flash = require('connect-flash');

// passport
const passport = require('passport');

// dotenv
require('dotenv').config();

// router
const pageRouter = require('./routes/page');

//login
const authRouter = require('./routes/auth');
const postRouter = require('./routes/post');
const userRouter = require('./routes/user');
// db
const { sequelize } = require('./models');
// passport
const passportConfig = require('./passport');

// express
const app = express();

//db
sequelize.sync();
// passport
passportConfig(passport);

app.set('views', path.join(__dirname,'views'));
app.set('view engine','pug');
app.set('port', process.env.PORT || 8001);

app.use(morgan('dev'));
app.use(express.static(path.join(__dirname,'public')));
// img
app.use('/img', express.static(path.join(__dirname, 'uploads')));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use(cookieParser(process.env.COOKIE_SECRET));

app.use(cookieParser('nodebirdsecret'));
app.use(session({
  resave: false,
  saveUninitialized: false,
  secret:'nodebirdsecret',
  secret: process.env.COOKIE_SECRET,
  cookie: {
    httpOnly: true,
    secure: false,
  },
}));
app.use(flash());

// passport
app.use(passport.initialize());
app.use(passport.session());

app.use('/', pageRouter);
//login
app.use('/auth', authRouter);
app.use('/post', postRouter);
app.use('/user', userRouter);

app.use((req, res, next) => {
  const err = new Error('Not Found');
  err.status = 404;
  next(err);
});

app.use((err, req, res) => {
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') ==='development' ? err : {};
  res.status(err.status || 500);
  res.render('error');
});

app.listen(app.get('port'), () => {
    console.log(app.get('port'),'번 포트에서 대기 중');
});