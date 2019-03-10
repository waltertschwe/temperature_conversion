import React from "react";
import { Link } from 'react-router-dom'

const Header = props => {
  return (
    <nav className="navbar navbar-dark bg-dark">
       <Link to="/dashboard" className="navbar-brand">Dashboard</Link>
       <Link to="/temperature-tool" className="navbar-brand">Temperature Tool</Link>
    </nav>
  )
}

export default Header;
