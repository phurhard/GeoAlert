import React, { useState } from "react";
import { useContext } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "./AuthContext";

const SignUp = () => {
  const { loggedIn, setLoggedIn } = useContext(AuthContext);
  const [username, setUsername] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async (e) => {
    e.preventDefault();

    const response = await fetch("http://localhost:5000/api/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, firstname, lastname, email, password }),
    });

    if (response.ok) {
      console.log("OK");
    } else {
      // Handle authentication error
      console.log("Unable to create a new User");
    }

    // Clear the form fields after signup
    setUsername("");
    setFirstname("");
    setLastname("");
    setEmail("");
    setPassword("");
  };
  console.log(loggedIn);
  return (
    <div className="Signup-container">
      <p>Turn your wanderlust to a to-do list with <b>GeoAlert</b><br/><i>where your dreams meet destinations</i></p>
      <form className='signup-form' onSubmit={handleSignup}>
        <label className="signup-label">
          Username:
          <input
            type="text"
            className="signup-input"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <label className="signup-label">
          First Name:
          <input
            type="text"
            className="signup-input"
            value={firstname}
            onChange={(e) => setFirstname(e.target.value)}
          />
        </label>
        <label className="signup-label">
          Last Name:
          <input
            type="text"
            className="signup-input"
            value={lastname}
            onChange={(e) => setLastname(e.target.value)}
          />
        </label>
        <label className="signup-label">
          Email:
          <input
            type="email"
            className="signup-input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <label className="signup-label">
          Password:
          <input
            type="password"
            className="signup-input"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <button className="signup-btn" type="submit">Sign Up</button>
      </form>
      <p className="login">Have an account? <span>
      <Link to="/login">Log In</Link>
          </span></p>
    </div>
  );
};

export default SignUp;
