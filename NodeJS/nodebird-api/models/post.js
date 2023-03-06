const Sequelize = require('sequelize');

module.exports = class Post extends Sequelize.Model {
  static init(sequelize) {
    return super.init({
      content: {
        type: Sequelize.STRING(140),
        allowNull: false,
      },
      img: {
        type: Sequelize.STRING(200),
        allowNull: true,
      },
    }, {
      sequelize,
      timestamps: true,
      underscored: false,
      modelName: 'Post',
      tableName: 'posts',
      paranoid: false,
      charset: 'utf8mb4',
      collate: 'utf8mb4_general_ci',
    });
  }

  static associate(db) {
    db.Post.belongsTo(db.User);
    db.Post.belongsToMany(db.Hashtag, { through: 'PostHashtag' });
  }
};

// module.exports = (sequelize, DataTypes) => (
//     sequelize.define('post', {
//         content: {
//             type: DataTypes.STRING(140),
//             allowNull: false,
//         }, 
//         img: {
//             type: DataTypes.STRING(200),
//             allowNull: true,
//         },
//     }, {
//         timestamps: true,
//         paranoid: true,
//     }) 
// );