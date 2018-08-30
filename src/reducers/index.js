import * as types from '../actions/ActionTypes';
// 3 immutable 사용하긔
import { Map, List } from 'immutable';

// 배열로서 같이 관리를 해야하기 때문에 합침
const initialState = Map({
    counters: List([
        Map({
            color: 'black',
            number: 0
        })
    ])
});


// push or pop을 쓰지 못하는 이유 : redux의 2법칙 - state는 read-only
// ... (spread operator)을 사용 or .slice()를 사용해서 배열을 잘라 새로 생성해야함.
// 원본은 건드려서는 안된다!

// immutable은 immutability의 규칙에 따르므로, push와 pop을 자유롭게 사용할 수 있음!!
function counter(state = initialState, action) {

    const counters = state.get('counters');

    switch (action.type) {

        // add
        case types.CREATE:
            return state.set('counters', counters.push(Map({
            // return state.set('counters', counters.unshift(Map({
                color: action.color,
                number: 0
            })));

        // remove   
        case types.REMOVE:
            return state.set('counters', counters.pop());
            // return state.set('counters', counters.shift());

        // increment
        case types.INCREMENT:
            return state.set('counters', 
                counters.update(
                    action.index,
                    (counter) => counter.set('number', counter.get('number') + 1)
            ));

        // decrement
        case types.DECREMENT:
            return state.set('counters', 
                counters.update(
                    action.index,
                    (counter) => counter.set('number', counter.get('number') - 1)
            ));
            
        // setColor
        case types.SET_COLOR:
            return state.set('counters',
                counters.update(
                    action.index,
                    (counter) => counter.set('color', action.color))
            );
        default:
            return state;
    }
};

export default counter;