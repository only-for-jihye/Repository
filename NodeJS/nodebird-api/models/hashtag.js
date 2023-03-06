const Sequelize = require('sequelize');

module.exports = class Hashtag extends Sequelize.Model {
  static init(sequelize) {
    return super.init({
      title: {
        type: Sequelize.STRING(15),
        allowNull: false,
        unique: true,
      },
    }, {
      sequelize,
      timestamps: true,
      underscored: false,
      modelName: 'Hashtag',
      tableName: 'hashtags',
      paranoid: false,
      charset: 'utf8mb4',
      collate: 'utf8mb4_general_ci',
    });
  }

  static associate(db) {
    db.Hashtag.belongsToMany(db.Post, { through: 'PostHashtag' });
  }
};


// module.exports = (sequelize, DataTypes) => (
//     sequelize.define('hashtag', {
//         title: {
//             type: DataTypes.STRING(15),
//             allowNull: false,
//             unique: true,
//         }, 
//     }, {
//         timestamps: true,
//         paranoid: true,
//     })
// );