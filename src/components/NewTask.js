import React, { useState } from "react";
import { Link } from "react-router-dom";

// eslint-disable-next-line no-unused-vars
import NewLocation from "./NewLocation";
import useUser from "./getUser";
function NewTask() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [time, setTime] = useState("");
  const token = JSON.parse(localStorage.getItem('token'));
  const access_token = token.access_token;
  const profile = useUser(access_token);
  const [date, setDate] = useState("");

  const newTask = async (e) => {
    e.preventDefault();
    const today = `${date}T${time}`
    const due_date = new Date(today);

    if (profile){
    const response = await fetch(`http://localhost:5000/api/${profile.username}/todo`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title, description, due_date}),
    });
    if (response.ok) {
      console.log("New task created");
      alert("New task created");
    } else {
      // Handle authentication error
      console.log("Unable to create a new task");
      alert("Unable to create a new task");
    }
    console.log(title, description, due_date);
  }
    // clear the inputs field after adding a new task
    setTime("");
    setTitle("");
    setDate("");
    setDescription("");
  }
  return (
    <>
      <div className="main add-location">
        <Link to="/">Return to home</Link>
        {/* will change the link and page such that after adding a new task it automatically returns to the home page */}
      </div>
      <div className="main newtask-container ">
        <h5>Add a new Task</h5>
        <form>
          <div className="mb-3">
            <label htmlFor="title" className="form-label">
              Title
            </label>

            <input
              type="text"
              className="form-control"
              id="title"
              placeholder=""
              name="task-value"
              value={title}
            onChange={(e) => setTitle(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="desc" className="form-label">
              Description
            </label>
            <textarea
              type="text"
              className="form-control"
              id="desc"
              placeholder=""
              value={description}
            onChange={(e) => setDescription(e.target.value)}
            name="description"
            ></textarea>
          </div>
          <div className="row mb-3">
            <label htmlFor="tdate" className="form-label">
              Duration
            </label>
            <div className="col-8">
              <input
                type="date"
                className="form-control"
                id="tdate"
                placeholder=""
                name="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
              />
            </div>
            <div className="col-4">
              <input
                type="time"
                className="form-control"
                id="ttime"
                placeholder=""
                name="time"
                value={time}
                onChange={(e) => setTime(e.target.value)}
              />{" "}
            </div>
          </div>
        </form>
        <p>Add Location?</p>
        <div className="d-flex justify-content-end">
          <button className="btn" onClick={newTask}>ADD TASK</button>
        </div>
      </div>
    </>
  );
}

export default NewTask;
