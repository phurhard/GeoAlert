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

function App() {
  const { loggedIn } = useContext(AuthContext);

  return (
    <AuthProvider>
      <div className="container-fluid g-0 main-container">
        <Router>
          {/* <Header /> */}
          <Routes>
            <Route
              path="/"
              element={!loggedIn ? <Home /> : <Navigate to="/login" replace />}
            />
            <Route
              path="/login"
              element={!loggedIn ? <Navigate to="/" replace /> : <Login />}
            />
            {/* <Route path="/login" element={<Login />} /> */}
            <Route
              path="/todolist"
              element={
                !loggedIn ? <TodoList /> : <Navigate to="/login" replace />
              }
            />
            <Route
              path="/newtask"
              element={
                !loggedIn ? <NewTask /> : <Navigate to="/login" replace />
              }
            />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/*" element="<Error />" />
          </Routes>{" "}
        </Router>
      </div>
    </AuthProvider>
  );
}

export default App;
