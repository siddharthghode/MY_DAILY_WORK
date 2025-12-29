import {Link} from "react-router-dom";

export default function Navbar()
{
    return (
        <nav>
            <Link to="/">Home</Link>
         |  <Link to="/Books">Books</Link>
          {/* | <Link to="/BookCard">BookCard</Link> */}
        </nav>
    );
}