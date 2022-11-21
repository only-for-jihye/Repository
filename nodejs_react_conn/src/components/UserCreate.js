import React, { Component } from 'react';
import axios from 'axios';

class UserCreate extends Component {

    state = {
        name: '',
        age: '',
        married: false
    }

    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        });
        console.log([e.target.name], e.target.value)
    }

    create = () => {
        axios.post('http://localhost:3000/users/', {
            name: this.state.name,
            age: this.state.age,
            married: this.state.married
        })
        .then((res) => {
            console.log(res);
        })
        .catch((e) => {
            console.error(e);
        });
    }

    checkHandler = (e) => {
        this.setState({
            [e.target.name]: e.target.checked
        });
        console.log([e.target.name], e.target.checked)
    }

    onReset = (e) => {
        this.setState({
            name: ''
        });
        console.log(this.state.name);
    }

    render () {
        return (
            <>
                <div>
                    name : <input placeholder='name' onChange={this.handleChange} name='name'/><br/>
                    age : <input placeholder='age' onChange={this.handleChange} name='age'/><br/>
                    married : <input type='checkbox' onChange={this.checkHandler} name='married'/><br/>
                </div>
                <button type='submit' onClick={this.create}>create...</button>
                <button onClick={this.onReset}>reset...</button>
            </>
        );
    }
}

export default UserCreate;