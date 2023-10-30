import { useState, useEffect } from "react";
import useUser from "./getUser";

const useTodos = () => {
    const token = JSON.parse(localStorage.getItem('token'));
  const access_token = token.access_token;
  const profile = useUser(access_token);
  const [todos, setTodos] = useState(null);
  
  useEffect(()  => {
    if (profile){
      fetch(`http://localhost:5000/api/${profile.username}/todos`)
       .then(res => {
        // console.log(res);
        if (!res.ok){
          throw Error('Unable to get todos from server');
        }
        return res.json();
       })
       .then(data => {
        setTodos(data)})

       .catch(err => {console.log('Error: ',err.message)})
    }

  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [profile]);
  // need to make the react only render once loaded and whenever the page chhanges or needs to be rerendered, not every time
  return todos
}
export default useTodos