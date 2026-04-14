    const config = {
      development: {
        API_URL: 'http://localhost:8000/api',
        DEBUG: true,
      },
      production: {
        API_URL: 'https://elmeudomini.com/api',
        DEBUG: false,
      }
    };
     
    const env = process.env.NODE_ENV || 'development';
    export default config[env];

