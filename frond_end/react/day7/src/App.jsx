import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/navbar";
import Home from "./pages/home";
import ImagePage from "./pages/image"; 



export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
        <Routes>
        <Route path="/" element={<Home  />} />
        <Route path="/image" element={<ImagePage />} />
        </Routes>
    </BrowserRouter>
  );
}