import React from 'react';
import styles from './Button.scss';
import classNames from 'classnames/bind';

const cx = classNames.bind(styles);

/*
    rest는 나중에 이 컴포넌트가 받을 모든 props를 명시함
    비구조화 할당 문법에서 ...foo 형식으로 입력하면 비구조화 할당을 할 때 따로 지정하지 않은 것들은 모두 foo 객체에 담김
    JSX를 렌더링 하는 부분에 { ...rest }를 넣어준 의미는 객체 안에 있는 모든 값을 해당 DOM/컴포넌트의 props로 지정한다는 의미
    예를 들어, rest 객체 안에 onClick과 style이 들어 있다면, <div onClick={onClick} style={style}>과 같은 형식으로 렌더링 됨
    컴포넌트에 전달하는 props를 별도 작업 없이 그대로 DOM에 전달할 수 있음
*/
const Button = ({children, ...rest}) => { 
    return (
        <div className={cx('button')} {...rest}>
            {children}
        </div>
    );
};

export default Button;