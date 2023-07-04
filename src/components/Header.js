import React from "react";
import hamburger from "./hamburger";

function Header() {
  return (
    <header>
      <nav className="row ">
        <div className="avatar col-2 g-0">
          <img src="#" alt="avatar"></img>
        </div>
        <div className="greeting-date col-9 g-0">
          <div className="greetings">
            <h3>Hello, Faruk</h3>
          </div>
          <div className="date">20th-May-2098</div>
        </div>
        <div className="col d-flex justify-content-end">
          <hamburger />
          <div className="box "></div>
        </div>
      </nav>
    </header>
  );
}

export default Header;
