import React, { Component } from 'react';
import { Route } from 'react-router-dom'
import './App.css';

/* Layout Files */
import Header from './layout/Header'

/* Import Containers */
import TemperatureToolContainer from "./containers/TemperatureToolContainer"


const TemperatureTool = () => (
    <TemperatureToolContainer />
)

const Dashboard = () => (
    <div className="mt-5 ml-5">
      <h3>Dashboard</h3>
    </div>
)

class App extends Component {
  render() {
    return (
      <div>
        <Header />
        <Route path="/temperature-tool" component={TemperatureTool} />
        <Route path="/dashboard" component={Dashboard} />
      </div>
    );
  }
}

export default App;
