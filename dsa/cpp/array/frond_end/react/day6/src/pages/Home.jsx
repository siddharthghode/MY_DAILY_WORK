import Button from "../components/Button";

function Home() {
  function handleClick() {
    alert("Button clicked!");
  }

  return (
    <div>
      <h1>Home Page</h1>

      <Button text="Click Me" onClick={handleClick} />
      <Button text="Delete" onClick={() => alert("Deleted")} />
    </div>
  );
}

export default Home;

