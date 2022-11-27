const KakaoStrategy = require('passport-kakao').Strategy;
const { User } = require('../models');

module.exports = (passport) => {
    passport.use(new KakaoStrategy({
        clientID: process.env.KAKAO_ID, 
        callbackURL:'/auth/kakao/callback',
    }, async (accessToken, refreshToken, profile, done) => { 
        console.log('kakao profile', profile);
        try {
            const exUser = await User.findOne({ where: { snsId: profile.id, provider:'kakao' } });
            //const exUser = await User.find({ where: { snsId: kakao_account.profile, provider:'kakao' } });
            if (exUser) {
                done(null, exUser);
            } else {
                const newUser = await User.create({
                    email: profile._json && profile._json.kakao_account.email,
                    //email: profile._json.kakao_acccount.email,
                    nick: profile.displayName,
                    snsId: profile.id,
                    provider:'kakao',
                });
                done(null, newUser);
            }
        } catch (error) {
            console.error(error);
            done(error);
        }
    }))
};

/*
kakao profile {
  provider: 'kakao',
  id: 2551038610,
  username: '원종수',
  displayName: '원종수',
  _raw: '{"id":2551038610,"connected_at":"2022-11-26T10:25:40Z","properties":{"nickname":"원종수","profile_image":"http://k.kakaocdn.net/dn/ruzYv/btrRXfSTYGZ/ozlfBxRgR0UHWdN6qfaOJ0/img_640x640.jpg","thumbnail_image":"http://k.kakaocdn.net/dn/ruzYv/btrRXfSTYGZ/ozlfBxRgR0UHWdN6qfaOJ0/img_110x110.jpg"},"kakao_account":{"profile_nickname_needs_agreement":false,"profile_image_needs_agreement":false,"profile":{"nickname":"원종수","thumbnail_image_url":"http://k.kakaocdn.net/dn/ruzYv/btrRXfSTYGZ/ozlfBxRgR0UHWdN6qfaOJ0/img_110x110.jpg","profile_image_url":"http://k.kakaocdn.net/dn/ruzYv/btrRXfSTYGZ/ozlfBxRgR0UHWdN6qfaOJ0/img_640x640.jpg","is_default_image":false},"has_email":true,"email_needs_agreement":false,"is_email_valid":true,"is_email_verified":true,"email":"s00@kakao.com"}}',
  _json: {
    id: 2551038610,
    connected_at: '2022-11-26T10:25:40Z',
    properties: {
      nickname: '원종수',
      profile_image: 'http://k.kakaocdn.net/dn/ruzYv/btrRXfSTYGZ/ozlfBxRgR0UHWdN6qfaOJ0/img_640x640.jpg',
      thumbnail_image: 'http://k.kakaocdn.net/dn/ruzYv/btrRXfSTYGZ/ozlfBxRgR0UHWdN6qfaOJ0/img_110x110.jpg'
    },
    kakao_account: {
      profile_nickname_needs_agreement: false,
      profile_image_needs_agreement: false,
      profile: [Object],
      has_email: true,
      email_needs_agreement: false,
      is_email_valid: true,
      is_email_verified: true,
      email: 's00@kakao.com'
    }
  }
}
*/