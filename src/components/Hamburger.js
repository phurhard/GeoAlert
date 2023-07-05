import React, { useState } from "react";
import "../App.css";

const Hamburger = () => {
  const [isOpen, setIsOpen] = useState(false);

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="App">
      <div
        className={`nav-icon1 ${isOpen ? "open" : ""}`}
        onClick={handleToggle}
      >
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div className={`menu ${isOpen ? "open" : ""}`}>
        <span className="close" onClick={handleToggle}>
          x
        </span>
        <ul>
          <li>Home</li>
          <li>About</li>
          <li>Contact</li>
        </ul>
      </div>
    </div>
  );
};

export default Hamburger;
