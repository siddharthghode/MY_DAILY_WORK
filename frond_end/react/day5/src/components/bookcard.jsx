export default function BookCard({ title, author }) {
  return (
    <div style={{ border: "1px solid #ccc", padding: "10px", margin: "10px 0" }}>
      <h3>{title}</h3>
      <p>{author}</p>
    </div>
  );
}
