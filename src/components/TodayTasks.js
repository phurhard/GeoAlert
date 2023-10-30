import React from "react";
import Todaytask from "./Todaytask";
import TodayMap from "./TodayMap";

// import { Link } from "react-router-dom";
function TodayTasks() {
  return (
    <>
      
      <div>
        <Todaytask />

        <TodayMap />
      </div>
    </>
  );
}

export default TodayTasks;
