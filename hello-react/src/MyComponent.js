import React, { Component } from "react";
import PropTypes from 'prop-types';

// class MyComponent extends Component {
//     render() {
//         return (
//             <div>
//                 Hi, My name is {this.props.name}.
//             </div>
//         )
//     }
// }

// MyComponent.defaultProps = {
//     name: 'Soo'
// }

// 또는
class MyComponent extends Component {
    static defaultProps = {
        name: 'aoo'
    }
    static propTypes = {
        name: PropTypes.string,
        age: PropTypes.number.isRequired 
    }
    constructor(props) {
        super(props);
        this.state = {
            number: 0
        }
    }
    render() {
        return (
            <div>
                <p>안녕 나는 {this.props.name}.</p>
                <p>내 나이는 {this.props.age}.</p>
                <p>숫자 : {this.state.number}</p>
                <button onClick={() => {
                    this.setState({
                        number: this.state.number + 1
                    })
                }}>더하기</button>
            </div>
        )
    }
}

// MyComponent.PropTypes = {
//     name: PropTypes.string
// }


export default MyComponent;
