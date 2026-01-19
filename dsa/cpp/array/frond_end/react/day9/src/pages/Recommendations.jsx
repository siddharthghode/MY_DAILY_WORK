import { useState } from "react";

export default function Recommendations() {
  const [loaded, setLoaded] = useState(false);

  return (
    <div>
      <h1>Recommendations</h1>

      {!loaded && <p>Click the button to load recommendations</p>}
      {loaded && <p>Recommended books loaded!</p>}

      <button onClick={() => setLoaded(true)}>
        Load Recommendations
      </button>
    </div>
  );
}
