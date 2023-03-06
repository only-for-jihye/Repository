import React, { Component } from 'react'; 

import CounterListContainer from './CounterListContainer';

import Buttons from '../components/Buttons';

import { connect } from 'react-redux';
import * as actions from '../actions';

import { getRandomColor } from '../utils';

class App extends Component { 

    render() {

        const { onCreate, onRemove } = this.props;

        return(
            <div className="App">
                <Buttons 
                    onCreate={onCreate}
                    onRemove={onRemove}
                />
                <CounterListContainer />
            </div>
        );
    }
}

// state값은 할 게 없으므로 mapStateToProps는 안써도 됌

const mapDispatchToProps = (dispatch) => ({
    onCreate: () => dispatch(actions.create(getRandomColor())),
    onRemove: (index) => dispatch(actions.remove(index))
});

// 안썼으니까 null
export default connect(null, mapDispatchToProps)(App);