import React from 'react';
import PropTypes from 'prop-types';

import './Buttons.css';

const Buttons = ({ onCreate, onRemove }) => {
    return (
        <div className="Buttons">
            <div className="btn add" onClick={onCreate}>
                생성
            </div>
            <div className="btn remove" onClick={onRemove}>
                제거
            </div>
        </div>
    );
};

Buttons.PropTypes={
    onCreate: PropTypes.func,
    onRemove: PropTypes.func
};

Buttons.defaultProps={
    onCreate: () => console.warn('onCreate is not defined'),
    onRemove: () => console.warn('onRemove is not defined')
};

export default Buttons;