import React from "react";
import { BrowserRouter as Link } from 'react-router-dom'

function NewTask() {
  return (
    <div className="main newtask-container">
      <h5>Add a new Task</h5>
      <form method="POST" action="127.0.0.1:5000/api">
        <div class="mb-3">
          <label for="title" className="form-label">
            Title
          </label>
          <input
            type="text"
            className="form-control"
            id="title"
            placeholder=""
            name="task-value"
          />
        </div>
        <div className="mb-3">
          <label for="desc" className="form-label">
            Description
          </label>
          <textarea
            type="text"
            className="form-control"
            id="desc"
            placeholder=""
            name="description"
          ></textarea>
        </div>
        <div className="row mb-3">
          <label for="tdate" className="form-label">
            Duration
          </label>
          <div className="col-8">
            <input
              type="date"
              className="form-control"
              id="tdate"
              placeholder=""
              name="date"
            />
          </div>
          <div className="col-4">
            <input
              type="time"
              className="form-control"
              id="ttime"
              placeholder=""
              name="time"
            />{" "}
          </div>
        </div>
      </form>
      <p><Link to='/location'>Add Location?</Link></p>
      {/* Make this add location clickable so that when it is
      clicked it redirect to the page to add location */}
      <div className="d-flex justify-content-end">
        <button className=""><Link to='/todolist'>ADD TASK</Link></button>
        {/* the button above redirects to the page where all tasks are shown */}
      </div>
    </div>
  );
}

export default NewTask;
