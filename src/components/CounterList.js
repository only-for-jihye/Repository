import React from 'react';
import Counter from './Counter';
import PropTypes from 'prop-types';

import './CounterList.css';

const CounterList = ({ counters, onIncrement, onDecrement, onSetColor }) => {

    const counterList = counters.map( // map => return new array[];
        (counter, i) => (
            <Counter 
                key={i}
                index={i}
                {...counter} // { color: ~, number: ~ }
                onIncrement={onIncrement}
                onDecrement={onDecrement}
                onSetColor={onSetColor}
            />
        )
    ); //console.log(counter); 찍어보기
    return (
        <div className="CounterList">
            {counterList}
        </div>
    );
};

CounterList.propTypes = {
    counters: PropTypes.arrayOf(PropTypes.shape({
        color: PropTypes.string,
        number: PropTypes.number
    })),
    onIncrement: PropTypes.func,
    onDecrement: PropTypes.func,
    onSetColor: PropTypes.func
};

CounterList.defaultProps = {
    counters: [],
    onIncrement: () => console.warn('onIncrement is not defined'),
    onDecrement: () => console.warn('onDecrement is not defined'),
    onSetColor: () => console.warn('onIncrement is not defined')
};

export default CounterList;