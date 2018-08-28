import React from 'react'; 
import PropTypes from 'prop-types';
import './Counter.css';

const propTypes = { 
    number: PropTypes.number,
    color: PropTypes.string,
    onIncrement: PropTypes.func,
    onDecrement: PropTypes.func,
    onSetColor: PropTypes.func
};

const defaultProps = { 
    number: -1,
    color: 'black',
    onIncrement: () => console.warn('onIncrement is not defined'),
    onDecrement: () => console.warn('onDecrement is not defined'),
    onSetColor: () => console.warn('onSetColor is not defined')
};


const Counter = ({ number, color, onIncrement, onDecrement, onSetColor }) => {
    return (
        <div
            className="Counter"
            onClick={onIncrement}
            onContextMenu={
                (e) => {
                    e.preventDefault(); // lock mouse right button menu
                    onDecrement();
                }
            }
            onDoubleClick={onSetColor}
            style={{ backgroundColor: color }}>
                {number}
        </div>
    );
};


Counter.propTypes = propTypes;
Counter.defaultProps = defaultProps;

export default Counter;