import React, { useState, useEffect, useContext } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Home from "./components/Home";
import TodoList from "./components/TodoList";
import NewTask from "./components/NewTask";
import Header from "./components/Header";
import Login from "./components/Login";
import { AuthProvider, AuthContext } from "./components/AuthContext";

function App() {
  const { loggedIn } = useContext(AuthContext);

  const PrivateRoute = ({ element: Component, ...rest }) => {
    return loggedIn ? (
      <Route element={<Component />} {...rest} />
    ) : (
      <Navigate to="/login" replace />
    );
  };

  return (
    <div className="container-fluid g-0 main-container">
      <AuthProvider>
        <Router>
          <Header />
          <Routes>
            <Route
              path="/"
              element={loggedIn ? <Home /> : <Navigate to="/login" replace />}
            />
            <Route
              path="/login"
              element={loggedIn ? <Navigate to="/" replace /> : <Login />}
            />
            <PrivateRoute path="/todolist" element={TodoList} />
            <PrivateRoute path="/newtask" element={NewTask} />
          </Routes>
        </Router>
      </AuthProvider>
    </div>
  );
}

export default App;
