import { BrowserRouter, Route, Routes } from "react-router-dom";
import './App.css';
import Navbar from "./components/navbar";
import Home from "./pages/home";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<div><h1>this is about page</h1></div>} />
      </Routes>
    </BrowserRouter>
        );
   }

export default App


