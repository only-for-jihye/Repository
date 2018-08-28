import { combineReducers } from 'redux';

import color from './color';
import number from './number';

const reducers = combineReducers({
    numberData: number,
    colorData: color
});

export default reducers;