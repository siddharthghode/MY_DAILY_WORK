import { useState } from "react";

export default function Home() {
  const [showMsg, setShowMsg] = useState(true);

  return (
    <div>
      <h1>Home Page</h1>

      {showMsg && <p>Welcome to the Book Recommendation System</p>}

      <button onClick={() => setShowMsg(!showMsg)}>
        Toggle Message
      </button>
    </div>
  );
}
