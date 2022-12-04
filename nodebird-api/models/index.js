const Sequelize = require('sequelize');
const env = process.env.NODE_ENV || 'development';
const config = require('../config/config')[env];
const User = require('./user');
const Post = require('./post');
const Hashtag = require('./hashtag');
const Domain = require('./domain');

const db = {};
const sequelize = new Sequelize(
  config.database, config.username, config.password, config,
);

db.sequelize = sequelize;
db.User = User;
db.Post = Post;
db.Hashtag = Hashtag;
db.Domain = Domain;

User.init(sequelize);
Post.init(sequelize);
Hashtag.init(sequelize);
Domain.init(sequelize);

User.associate(db);
Post.associate(db);
Hashtag.associate(db);
Domain.associate(db);

module.exports = db;

// const Sequelize = require('sequelize');
// const env = process.env.NODE_ENV ||'development';
// const config = require('../config/config')[env];

// const db = {};

// const sequelize = new Sequelize(
//   config.database, config.username, config.password, config,
// );

// db.sequelize = sequelize;
// db.Sequelize = Sequelize;
// //db.User = require('./user')(sequelize, Sequelize);
// const User = require('./user');
// db.USER = User;
// User.init(sequelize);

// db.Post = require('./post')(sequelize, Sequelize);

// db.Hashtag = require('./hashtag')(sequelize, Sequelize);
// db.Domain = require('./domain')(sequelize, Sequelize);

// //db.User.hasMany(db.Post);
// //db.Post.belongsTo(db.User);
// User.associate(db);
// Post.associate(db);

// db.Post.belongsToMany(db.Hashtag, { through:'PostHashtag' });
// db.Hashtag.belongsToMany(db.Post, { through:'PostHashtag' });

// db.User.belongsToMany(db.User, {
//   foreignKey:'followingId',
//   as:'Followers',
//   through:'Follow',
// });

// db.User.belongsToMany(db.User, {
//   foreignKey:'followerId',
//   as:'Followings',
//   through:'Follow',
// });

// //db.User.hasMany(db.Domain);
// User.associate(db);
// //db.Domain.belongsTo(db.User);
// Domain.associate(db);

// module.exports = db;

/*
'use strict';

const fs = require('fs');
const path = require('path');
const Sequelize = require('sequelize');
const process = require('process');
const basename = path.basename(__filename);
const env = process.env.NODE_ENV || 'development';
const config = require(__dirname + '/../config/config.json')[env];
const db = {};

let sequelize;
if (config.use_env_variable) {
  sequelize = new Sequelize(process.env[config.use_env_variable], config);
} else {
  sequelize = new Sequelize(config.database, config.username, config.password, config);
}

fs
  .readdirSync(__dirname)
  .filter(file => {
    return (file.indexOf('.') !== 0) && (file !== basename) && (file.slice(-3) === '.js');
  })
  .forEach(file => {
    const model = require(path.join(__dirname, file))(sequelize, Sequelize.DataTypes);
    db[model.name] = model;
  });

Object.keys(db).forEach(modelName => {
  if (db[modelName].associate) {
    db[modelName].associate(db);
  }
});

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db;
*/