export default function BookCard({ title, author }) {
  return (
    <div style={{ border: "1px solid #e40808ff", padding: "10px", marginBottom: "10px" }}>
      <h3>{title}</h3>
      <p>Author: {author}</p>
    </div>
  );
}
