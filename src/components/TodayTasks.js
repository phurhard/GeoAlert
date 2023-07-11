import React from "react";
import Todaytask from "./Todaytask";
import TodayMap from "./TodayMap";
import Header from "./Header";
// import { Link } from "react-router-dom";
function TodayTasks() {
  return (
    <>
      {/* <Header /> */}
      <div>
        <Todaytask />
        <Todaytask />
        <Todaytask />
        <Todaytask />

        <TodayMap />
      </div>
    </>
  );
}

export default TodayTasks;
