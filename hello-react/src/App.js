// import React, { Component, Fragment } from 'react';
import React, { Component } from 'react';

import MyComponent from './MyComponent';

class App extends Component {
  render() {
    return (
      //<MyComponent name="React"/>
      // <MyComponent/>
      <MyComponent name="react" age={4}/>
    )
  }
}

export default App;
