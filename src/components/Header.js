import React, { useEffect } from "react";
import Hamburger from "./Hamburger";
import { useState } from "react";
import useUser from "./getUser";


function Header() {
  const [username, setUsername] = useState("Guest");
  const token = JSON.parse(localStorage.getItem('token'));
  const access_token = token.access_token;
  const profile = useUser(access_token);
  
  
  useEffect(()  => {
    if (profile){
      setUsername(profile.username); 
    }

  }, [profile]);
  
  return (
    <header>
      <nav className="row ">
        <div className="avatar col-2 g-0">
          <img id="hero-img" src="https://www.befunky.com/images/prismic/1f427434-7ca0-46b2-b5d1-7d31843859b6_funky-focus-red-flower-field-after.jpeg?auto=avif,webp&format=jpg&width=863" alt="avatar"></img>
        </div>
        <div className="greeting-date col-8 g-0">
          <div className="greetings">
            <h3>Hello, { username }</h3>
          </div>
          <div className="date">today date and time should be here</div>
        </div>
        <div className="col-2 g-0 d-flex hamburger justify-content-center">
          <Hamburger />
        </div>
      </nav>
    </header>
  );
}

export default Header;
