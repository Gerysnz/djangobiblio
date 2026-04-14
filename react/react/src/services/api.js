    import config from '../config';
     
    const API_BASE_URL = config.API_URL;
     
    export const getBooks = () => {
      console.log('cridant API...');
      return fetch(API_BASE_URL+"/llibres")
        .then((response) => {
          if (!response.ok) {
            throw new Error("Error l'obtenir els llibres");
          }
          return response.json();
        })
        .catch((error) => {
          console.error('Error en la API:', error);
          return [];
        });
    };

