import React, { useContext, useState } from "react";
import { AuthContext } from "./AuthContext";
import { useNavigate, Link } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { loggedIn, setLoggedIn } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    // Send a POST request to the authentication endpoint
    const response = await fetch("http://localhost:5000/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });

    if (response.ok) {
       const token = await response.json();

      // Store the token in local storage or session storage
      localStorage.setItem("token", JSON.stringify(token));
      console.log("Login");
      // console.log('token: ',JSON.parse(localStorage.getItem('token')));
      alert('Logged in');
      // Update the authentication state
      setLoggedIn(true);
      // console.log(loggedIn);
      navigate("/");
    } else {
      // Handle authentication error
      alert('Logged in failed');
      console.log("Login failed");
    }
  };

  return (
    <div className='login-container'>
      <form className='login-form' onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          className="input"
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          className="input"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button id="login-btn" type="submit">Login</button>
      </form>
      <p className="signUp">No account yet? <span>
      <Link to="/signup">Signup Now</Link>
          </span></p>
    </div>
  );
};

export default Login;
