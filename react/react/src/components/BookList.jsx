    import { useEffect, useState } from 'react';
    import { getBooks } from '../services/api';
    import BookItem from './BookItem';
    import imgReact from '../assets/react.svg';
     
    function BookList() {
      const [books, setBooks] = useState([]);
     
      useEffect(() => {
        getBooks().then((data) => setBooks(data));
      }, []);
     
      return (
        <div className="container">
          <img src={imgReact} />
          <h1>Llistat de llibres</h1>
          {books.length > 0 ? (
            books.map((book) => <BookItem key={book.id} book={book} />)
          ) : (
            <p>Encara no hi ha llibres...</p>
          )}
        </div>
      );
    }
     
    export default BookList;

