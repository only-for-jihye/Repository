module.exports = (sequelize, DataTypes) => {
    return sequelize.define('user', {
      name: {
        type: DataTypes.STRING(20), // MySQL varchar -> string
        allowNull: false,
        unique: true,
      },
      age: {
        type: DataTypes.INTEGER.UNSIGNED, // MySQL int -> integer // ZEROFILL 옵션 사용 필요 시, INTEGER.UNSIGNED.ZEROFILL 적용
        allowNull: false, // NOT NULL
      }, 
      married: {
        type: DataTypes.BOOLEAN, // MySQL tinyint -> boolean
        allowNull: false,
      },
      comment: {
        type: DataTypes.TEXT,
        allowNull: true,
      },
      created_at: {
        type: DataTypes.DATE, // MySQL datetime -> date
        allowNull: false,
        defaultValue: sequelize.literal('now()'),
      }, 
  }, {
    timestamps: false,
  });
 };