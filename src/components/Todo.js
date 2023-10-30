import React from "react";
import location from "../assets/images/location.svg";
import magicpen from "../assets/images/magicpen.svg";
import overdue from "../assets/images/overdue.svg";
import pending from "../assets/images/pending.svg";
import completed from "../assets/images/completed.svg";
import timer from "../assets/images/timer.svg";
import close from "../assets/images/close-circle.svg";
function Todo() {
  return (
    <div className="todo-container">
      <div className="row">
        <div className="col-1  "></div>
        <div className="item-title col-6  "> Get FoodStuffs</div>
        <div className="col-1  "></div>
        <div className="col-2 "></div>
        <div className="todo-status col-2 ">Pending</div>
      </div>
      <div className="row">
        <div className="item-check  col-1 "></div>
        <div className="item-duration  col-6 ">
          <div className="row -1">
            <div className="duration-icon text-center col-2 ">
              {" "}
              <img src={timer} alt="timer" />
            </div>
            <div className="duration col-10 ps-0 ">09:00am - 09:15am</div>
          </div>
        </div>
        <div className="todo-edit col-1 text-center ">
          <img src={magicpen} alt="" />
        </div>
        <div className="todo-delete col-1 text-center ">
          <img src={close} alt="" />
        </div>
        <div class="col-1"></div>
        <div className="todo-status-icon col-2  text-center">
          <img src={pending} alt="" />
        </div>
      </div>
      <div className="row ">
        <div className="col-1"></div>
        <div className="item-location  col-6 ">
          <div className="row">
            <div className="location-icon col-2  text-center ">
              {" "}
              <img src={location} alt="" />
            </div>
            <div className="location col-10  ps-0">Teepha's Store</div>
          </div>
        </div>
        <div className="col-3"></div>
      </div>
    </div>
  );
}

export default Todo;
