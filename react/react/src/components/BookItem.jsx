    import React, { useState } from 'react';
     
    function BookItem({ book }) {
      const [modalObert, setModalObert] = useState(false);
     
      function mostraDetalls() {
        setModalObert(true);
      }
     
      function tancaModal() {
        setModalObert(false);
      }
     
      return (
        <div className="book-card">
          <h3>{book.titol}</h3>
          <p>
            <strong>Autor:</strong> {book.autor}
          </p>
          <button onClick={mostraDetalls}>Detalls</button>
     
          {/* Modal */}
          {modalObert && (
            <div className="modal-overlay" onClick={tancaModal}>
              <div className="modal-content" onClick={e => e.stopPropagation()}>
                <div className="modal-header">
                  <h2>{book.titol}</h2>
                  <button className="close-btn" onClick={tancaModal}>×</button>
                </div>
                <div className="modal-body">
                  <p><strong>Autor:</strong> {book.autor}</p>
                  <p><strong>Data d'edició:</strong> {book.data_edicio || 'No disponible'}</p>
                  <p><strong>Gènere:</strong> {book.genere || 'No disponible'}</p>
                  <p><strong>Resum:</strong> {book.resum || 'Sense descripció'}</p>
                  {/* Afegeix més camps segons les propietats del teu objecte book */}
                </div>
                <div className="modal-footer">
                  <button onClick={tancaModal}>Tancar</button>
                </div>
              </div>
            </div>
          )}
        </div>
      );
    }
     
    export default BookItem;

