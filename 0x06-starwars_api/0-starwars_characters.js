#!/home/rugira/.nvm/versions/node/v21.7.1/bin/node
import request from 'request';

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body).name);
    });
  });
}

function printCharacters (movieId) {
  request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, (error, response, body) => {
    if (error) console.error(error);
    else {
      const characters = JSON.parse(body).characters;
      for (const url of characters) {
        getCharacterName(url).then(console.log);
      }
    }
  });
}

const movieId = process.argv[2];
printCharacters(movieId);
