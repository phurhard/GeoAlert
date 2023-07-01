import React from "react";
import Todo from "./Todo";
import Header from "./Header";
// import Add_button from "../assets/images/add-icon.png";
import { Link } from "react-router-dom";
function TodoList() {
  return (
    <div class="main">
      <div className="task-counts text-center">
        <div className="count">
          {" "}
          <h4>8/14</h4>
          <span className="d-inline-block">Tasks Completed</span>
        </div>
      </div>
      <div className="task-filter">
        <form className="d-flex mb-2">
          <div className="me-3">
            <input
              type="radio"
              id="all"
              name="task-filter"
              value="all"
              className="d-inline-block me-2"
            />
            <label for="all">All</label>
          </div>
          <div className="me-3">
            <input
              type="radio"
              id="completed"
              name="task-filter"
              value="completed"
              className="d-inline-block me-2"
            />
            <label for="completed">Completed</label>
          </div>
          <div className="me-3">
            <input
              type="radio"
              id="due-task"
              name="task-filter"
              value="due-task"
              className="d-inline-block me-2"
            />
            <label for="due-task">Due Dates</label>
          </div>
        </form>
      </div>
      <div className="row">
        <Todo />
        <Todo />
        <Todo />
        <Todo />
        <Todo />
        <Todo />
        <Todo />
        <Todo />
      </div>
      <div className="add-button text-center mt-3">
        <Link to="/newtask">
          {/* <img src={Add_button} alt="" height="60px" width="60px" /> */}
        </Link>{" "}
      </div>
    </div>
  );
}

export default TodoList;
