#!/usr/bin/node
const request = require('require');

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body).name);
    });
  });
}

function printCharacters (movieId) {
  request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
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
