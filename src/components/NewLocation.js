import React from "react";

function NewLocation() {
  // calling the foursquare places api
  // request =
  return (
    <div>
      <section className="go-back">
        <span>&lt; &nbsp; Back</span>
      </section>
      <section id="search">
        <label for="search-input">
          <i className="fa fa-search" aria-hidden="true"></i>
          <span className="sr-only">Search icons</span>
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
  );
}

export default NewLocation;
