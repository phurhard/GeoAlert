import React, { useState } from 'react';
import '../App.css';
import App from '../App'
import Home from './Home'
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

const Hamburger = () => {
  const [isOpen, setIsOpen] = useState(false);

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };

  return (
    <Router>
    <div className="App">
      <div className={`hamburger ${isOpen ? 'open' : ''}`} onClick={handleToggle}>
        <div className="line"></div>
        <div className="line"></div>
        <div className="line"></div>
      </div>
      <div className={`menu ${isOpen ? 'open' : ''}`}>
        <span className='close' onClick={handleToggle}>x</span>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
          <li>Contact</li>
        </ul>
      </div>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/about' element={<App />} />
      </Routes>
    </div>
    </Router>
  );
};

export default Hamburger;