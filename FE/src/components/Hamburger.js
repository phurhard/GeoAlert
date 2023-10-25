import React, { useState, useContext } from "react";
import "../App.css";
import { Link } from "react-router-dom";
import { AuthContext } from "./AuthContext";
const Hamburger = () => {
  const [isOpen, setIsOpen] = useState(false);
  const { loggedIn, setLoggedIn } = useContext(AuthContext);

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };
  const handleLogout = (e) => {
    e.preventDefault();
    // Remove the token from storage
    localStorage.removeItem("token");

    // Update the authentication state
    setLoggedIn(false);
    console.log(loggedIn);
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
      <ul className={`nav-links ${isOpen ? "open" : ""}`}>
        <li>
          <Link to="/">My Tasks</Link>
        </li>
        <li>
          <Link to="/locationbasedtask">Location Based Tasks</Link>
        </li>
        <li>
          <Link to="/newtask">New Task</Link>
        </li>
        <li>
          <Link to="/todotask">Profile</Link>
        </li>
        <li>
          <Link to="/login" onClick={handleLogout}>
            Log out
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default Hamburger;
