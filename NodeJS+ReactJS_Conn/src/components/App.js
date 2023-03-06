import React, { Component } from 'react';
import UserCreate from './UserCreate';
import UserList from './UserList';


class App extends Component {
    render() {
        return (
            <div>
                사용자 관리
                <UserCreate/>
                <UserList/>
            </div>
        );
    }
}

export default App;