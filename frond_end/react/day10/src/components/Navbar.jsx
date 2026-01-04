import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link> |{" "}
      <Link to="/books">Books</Link> |{" "}
      <Link to="/recommendations">Recommendations</Link> |{" "}
      <Link to="/counter">Counter</Link>
    </nav>
  );
}
