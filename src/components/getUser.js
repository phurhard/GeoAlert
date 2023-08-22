import { useState, useEffect } from "react";

const useUser = (token) => {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch("http://localhost:5000/api/profile", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "Authorization": 'Bearer ' + token
            },
            
          })
          .then(res => {
            if (!res.ok){
              throw Error('Unable to fetch profile from server');
            }
            return res.json();
          })
          .then(data => {
            setData(data);
        })
          .catch(error => console.log(error.message));
          
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);
    return data
}

export default useUser;