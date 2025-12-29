import BookCard from "../components/BookCard";

export default function Books() {
  const books = [
    { id: 1, title: "Clean Code", author: "Robert C. Martin" },
    { id: 2, title: "The Pragmatic Programmer", author: "Andrew Hunt" },
    { id: 3, title: "Design Patterns", author: "Erich Gamma" },
  ];

  return (
    <div>
      <h1>Books Page</h1>

      {books.map((book) => (
        <BookCard
          key={book.id}
          title={book.title}
          author={book.author}
        />
      ))}
    </div>
  );
}
