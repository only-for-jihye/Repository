import Counter from '../components/Counter';
import * as actions from '../actions';
import { connect } from 'react-redux';
import { getRandomColor } from '../utils';

// store의 state를 props로 매핑하여 연결
const mapStateToProps = (state) => ({
    number: state.numberData.number,
    color: state.colorData.color
});

// action을 dispatch하는 함수를 props로 연결
const mapDispatchToProps = (dispatch) => ({
    onIncrement: () => dispatch(actions.increment()),
    onDecrement: () => dispatch(actions.decrement()),
    onSetColor: () => {
        const color = getRandomColor();
        dispatch(actions.setColor(color));
    }
});

// store가 가진 state를 props로 엮고
// reducer에 action을 dispatch하는 함수를 props로 넘긴다.
// 즉, component에 props를 넣어주는 nonFunction가 반환되고, 
// param으로 Counter component를 가짐

const CounterContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(Counter);

export default CounterContainer;

// 이번 Container는 단순히 Redux와 연결하는 역할