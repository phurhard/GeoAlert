import "bootstrap/dist/css/bootstrap.css";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import TodoList from "./components/TodoList";
import NewTask from "./components/NewTask";
import Header from "./components/Header";

function App() {
  return (
    <div className="container-fluid g-0 main-container">
      <Header />
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/todolist" element={<TodoList />} />
          <Route path="/newtask" element={<NewTask />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
