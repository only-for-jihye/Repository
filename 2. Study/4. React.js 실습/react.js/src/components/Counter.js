import React from 'react'; 
import PropTypes from 'prop-types';
import './Counter.css';

const propTypes = { 
    index: PropTypes.number,
    number: PropTypes.number,
    color: PropTypes.string,
    onIncrement: PropTypes.func,
    onDecrement: PropTypes.func,
    onSetColor: PropTypes.func
};

const defaultProps = { 
    index: -1,
    number: -1,
    color: 'black',
    onIncrement: () => console.warn('onIncrement is not defined'),
    onDecrement: () => console.warn('onDecrement is not defined'),
    onSetColor: () => console.warn('onSetColor is not defined')
};


const Counter = ({ number, color, onIncrement, onDecrement, onSetColor, index }) => {
    return (
        <div
            className="Counter"
            onClick={() => onIncrement(index)} // 단순 props로 받다가 index가 추가되면서 각각의 이벤트가 발생할때
            onContextMenu={                    // 실행하는 function으로 바끔 => 각각 index를 param으로 넣어 실행
                (e) => {                        
                    e.preventDefault(); // lock mouse right button menu
                    onDecrement(index);
                }
            }
            onDoubleClick={() => onSetColor(index)}
            style={{ backgroundColor: color }}>
                {number}
        </div>
    );
};


Counter.propTypes = propTypes;
Counter.defaultProps = defaultProps;

export default Counter;