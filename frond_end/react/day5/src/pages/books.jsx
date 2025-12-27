import BookCard from "../components/bookcard";

export default function Books() {
  return (
    <div>
      <h1>Books Page</h1>

      <BookCard title="Clean Code" author="Robert C. Martin" />
      <BookCard title="The Pragmatic Programmer" author="Andrew Hunt" />
      <BookCard title="Design Patterns" author="Erich Gamma" />
    </div>
  );
} 
