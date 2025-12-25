import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link> |{" "}
      <Link to="/books">Books</Link> |{" "}
      <Link to="/about_us">About Us</Link> |{" "} 
      <Link to="/contact_us">Contact Us</Link>
    </nav>
  );
}
