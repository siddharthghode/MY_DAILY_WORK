import { BrowserRouter, Route, Routes } from "react-router-dom";


import Navbar from "./components/navbar";
import Home from "./pages/home";
import Books from "./pages/books";
import BookCard from "./components/bookcard";


function App()
{
  return(
        <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/books" element={<Books />} />
          <Route path="/bookcard" element={<BookCard />} />
        </Routes>
        </BrowserRouter>

  );
}
export default App;