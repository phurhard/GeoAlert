import React from "react";
import { Link } from "react-router-dom";
import no_task from "../assets/images/no-task.svg";
import useTodos from "./getTodos";

function Todaytask() {
  // fetch data from the database
  const todos = useTodos()
  const date = new Date();
  function dict(arg){
    if (arg === null) {return false;}
    else if (Object.values(arg).length === 0) {return false;}
    else {
      return true;
    }
  }
  return (
    <>
    { (() => {
      if (dict(todos)) {
    return <div className="task row ">
      { Object.values(todos).filter(todo => todo.due_date === date).map((todo)=> (
      <div className="tasks" key={ todo.id }>
        <div className="task-title col-5">{todo.title}<span>{todo.description}</span></div>
        <div className="task-time col-3">{todo.due_date}</div>
        <div className="task-location col-2">checker </div>
        <div className="task-status col-2">{todo.completed ? <span id="green"></span> : <span id="red"></span>}</div>
        {/* find a way to embed js code to check if completed is false should give a red color but if true should give a green color */}
      </div>
      ))}
    </div>} else {
      return <div className="main-no-item ">
      <p className="first-p">You don't have any tasks yet</p>
      <img src={no_task} alt="" style={{ width: "100%" }} />
      <p className="second-p">
        Tasks will appear as soon as you add them here
      </p>
      <div className="button-center btn">
        <button>
          {" "}
          <Link to="/newtask">Add Tasks</Link>
        </button>
      </div>
    </div>

    }
  })()}</>
  );
}

export default Todaytask;
