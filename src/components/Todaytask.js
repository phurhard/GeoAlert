import React from "react";
import { useEffect, useState } from 'react';
import useUser from "./getUser";

function Todaytask() {
  // fetch data from the database
  const token = JSON.parse(localStorage.getItem('token'));
  const access_token = token.access_token;
  const profile = useUser(access_token);
  
  useEffect(()  => {
    if (profile){
      fetch(`http://localhost:5000/api/${profile.username}/todos`)
       .then(res => {
        console.log(res);
        if (!res.ok){
          throw Error('Unable to get todos from server');
        }
        return res.json();
       })
       .then(data => {console.log(data)})

       .catch(err => {console.log(err.message)})
    }

  }, [profile]);
  return (
    <div className="task row ">
      <div className="task-title col-5">Take out the trash </div>
      <div className="task-time col-3">09:00am</div>
      <div className="task-location col-2"> Ajaokuta</div>

      <div className="task-status col-2"></div>
    </div>
  );
}

export default Todaytask;
