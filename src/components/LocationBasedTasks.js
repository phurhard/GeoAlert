import React from "react";
import Header from "./Header";
function LocationBasedTasks() {
  return (
    <>
      <Header />
      <div>
        <h3>All your location based tasks in one place</h3>
        <section id="search">
          <label for="search-input">
            <i class="fa fa-search" aria-hidden="true"></i>
            <span class="sr-only">Search icons</span>
          </label>
          <input
            id="search-input"
            className="form-control input-lg"
            placeHolder="Search icons"
            autoComplete="off"
            spellCheck="false"
            autoCorrect="off"
            tabIndex="1"
          />
        </section>
        <section className="map"></section>
        <section className="location-save">
          <div className="row"></div>
        </section>
      </div>
    </>
  );
}

export default LocationBasedTasks;
