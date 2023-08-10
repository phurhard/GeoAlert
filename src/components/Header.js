import React from "react";
import Hamburger from "./Hamburger";
import { useState } from "react";


function Header() {
  const [username, setUsername] = useState("Guest");
  // trying to set up the date  and time part
  // const [todayDate, setTodayDate] = useState(new Date());
  // // setting  the date
  // setInterval(() => {
  //   setTodayDate = new Date()
  // }, 1000);


  // calling the profile api

  const token = JSON.parse(localStorage.getItem('token'));
  const access_token = token.access_token;
  const profile = fetch("http://localhost:5000/api/profile", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "Authorization": 'Bearer ' + access_token
    },
    
  });
  profile.then(res => {return res.json();})
  .then(data => {
  console.log(data);
  setUsername(data.username);
})
  .catch(error => console.log(error));
  
  return (
    <header>
      <nav className="row ">
        <div className="avatar col-2 g-0">
          <img src="#" alt="avatar"></img>
        </div>
        <div className="greeting-date col-8 g-0">
          <div className="greetings">
            <h3>Hello, { username }</h3>
          </div>
          <div className="date">today date and time should be here</div>
        </div>
        <div className="col-2 g-0 d-flex justify-content-end">
          <Hamburger />
        </div>
      </nav>
    </header>
  );
}

export default Header;
