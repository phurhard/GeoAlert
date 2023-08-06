import React from "react";

import NewLocation from "./NewLocation";
function NewTask() {
  return (
    <>
      <div className="main add-location">
        <NewLocation />
      </div>
      <div className="main newtask-container d-none">
        <h5>Add a new Task</h5>
        <form>
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
        <p>Add Location?</p>
        <div className="d-flex justify-content-end">
          <button className="">ADD TASK</button>
        </div>
      </div>
    </>
  );
}

export default NewTask;
