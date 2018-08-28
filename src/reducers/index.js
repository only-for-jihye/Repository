import * as types from '../actions/ActionTypes';

// 배열로서 같이 관리를 해야하기 때문에 합침
const initialState = {
    counters: [
        {
            color: 'black',
            number: 0
        }
    ]
};


// push or pop을 쓰지 못하는 이유 : redux의 2법칙 - state는 read-only
// ... (spread operator)을 사용 or .slice()를 사용해서 배열을 잘라 새로 생성해야함.
// 원본은 건드려서는 안된다!
function counter(state = initialState, action) {

    const { counters } = state;

    switch (action.type) {
        // add
        case types.CREATE:
            return {
                counters: [
                    ...counters,
                    {
                        color: action.color,
                        number: 0
                    }
                ]
            };
        // remove   // splice는 원본을 건드리고, slice는 원본을 건드리지 않고 새로운 배열로 반환
        case types.REMOVE:
            return {
                counters: counters.slice(0, counters.length - 1)
            };
        // increment
        case types.INCREMENT:
            return {
                counters: [
                    ...counters.slice(0, action.index),                     // 시작부터 인덱스 전까지 짜르고
                    {
                        ...counters[action.index],
                        number: counters[action.index].number + 1           // 해당 인덱스의 number 증가
                    },
                    ...counters.slice(action.index + 1, counters.length)    // 인덱스 뒤부터 마지막까지 짤라 
                ]                                                           // 붙이면서 새로운 배열 생성
            };
        // decrement
        case types.DECREMENT:
            return {
                counters: [
                    ...counters.slice(0, action.index),                     
                    {
                        ...counters[action.index],
                        number: counters[action.index].number - 1           
                    },
                    ...counters.slice(action.index + 1, counters.length)    
                ]                                                           
            };
        // setColor
        case types.SET_COLOR:
            return {
                counters: [
                    ...counters.slice(0, action.index),                     
                    {
                        ...counters[action.index],
                        color: action.color           
                    },
                    ...counters.slice(action.index + 1, counters.length)    
                ]                                                           
            };
        default:
            return state;
    }
};

export default counter;