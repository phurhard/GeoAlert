import React, { useContext } from "react";
import "bootstrap/dist/css/bootstrap.css";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Home from "./components/Home";
import TodoList from "./components/TodoList";
import NewTask from "./components/NewTask";
// import Header from "./components/Header";
import Login from "./components/Login";
import SignUp from "./components/SignUp";
import { AuthProvider, AuthContext } from "./components/AuthContext";
import LocationBasedTasks from "./components/LocationBasedTasks";

function App() {
  const { loggedIn } = useContext(AuthContext);
  return (
    <div className="container-fluid g-0 main-container">
      <Router>
        <Routes>
          <Route
            path="/"
            element={!loggedIn ? <Navigate to="/login" replace /> : <Home />}
          />
          <Route
            path="/login"
            element={!loggedIn ? <Login /> : <Navigate to="/" replace />}
          />
          {/* <Route path="/login" element={<Login />} /> */}
          <Route
            path="/todolist"
            element={
              !loggedIn ? <Navigate to="/login" replace /> : <TodoList />
            }
          />
          <Route
            path="/newtask"
            element={!loggedIn ? <Navigate to="/login" replace /> : <NewTask />}
          />
          <Route
            path="/locationbasedtask"
            element={
              !loggedIn ? (
                <Navigate to="/login" replace />
              ) : (
                <LocationBasedTasks />
              )
            }
          />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/*" element="<Error />" />
        </Routes>{" "}
      </Router>
    </div>
  );
}

export default App;
