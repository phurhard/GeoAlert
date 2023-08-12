/* eslint-disable no-unused-vars */
import React, { useEffect, useState } from "react";
import TodayTasks from "./TodayTasks";
import Header from "./Header";
import TodoList from "./TodoList";
import NewTask from "./NewTask";
import MapLocation from "./MapLocation";
import { BrowserRouter as Route, Router, Link, Routes } from "react-router-dom";
import no_task from "../assets/images/no-task.svg";
function Home() {
  return (
    <>
      <Header />
      <div className="main">
        <div className="main-item">
          <div className="what-are-we">
            <h5>What are we doing today</h5>
          </div>
          <div className="today-task-container">
            <div className="today-task">
              <h6>Today's Tasks</h6>
            </div>
            <div className="today-task-head row">
              <div className="title col-5 g-0">Title</div>
              <div className="time col-3 g-0">Time</div>
              <div className="location col-2 g-0">Location</div>
              <div className="status col-2 g-0">Status</div>
            </div>
            <TodayTasks />
            <div className="show-all-tasks text-end ">
              <Link
                to="/todolist"
                className="link-underline link-underline-opacity-0"
              >
                Show all
              </Link>
            </div>
          </div>
          {/* <MapLocation /> */}
        </div>
        <div className="main-no-item d-none">
          <p className="first-p">You don't have any tasks yet</p>
          <img src={no_task} alt="" style={{ width: "100%" }} />
          <p className="second-p">
            Tasks will appear as soon as you add them here
          </p>
          <div className="button-center">
            <button>
              {" "}
              <Link to="/newtask">Add Tasks</Link>
            </button>
          </div>

          <div className="today-task-head row">
            <div className="title col-5 g-0">Title</div>
            <div className="time col-3 g-0">Time</div>
            <div className="location col-2 g-0">Location</div>
            <div className="status col-2 g-0">Status</div>
          </div>
          <TodayTasks />

          <div className="show-all-tasks text-end ">
            <Link
              to="/todolist"
              className="link-underline link-underline-opacity-0"
            >
              Show all
            </Link>
          </div>
          {/* this section holds the map showwing the current location of the use, will be updated with markers showing the location based tasks */}
          <div className="map markers-today">
            <MapLocation />
          </div>
        </div>
      </div>
    </>
  );
}

export default Home;
