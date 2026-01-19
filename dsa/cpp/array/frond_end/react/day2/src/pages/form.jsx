function Form() {
  return (
    <form>
      <h2>Simple Form</h2>

      <div>
        <label>Name:</label><br />
        <input type="text" placeholder="Enter your name" />
      </div>

      <br />

      <div>
        <label>Email:</label><br />
        <input type="email" placeholder="Enter your email" />
      </div>

      <br />

      <button type="submit">Submit</button>
    </form>
  );
}

export default Form;
