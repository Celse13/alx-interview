#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const movieURL = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function requestUrl (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, resonse, body) => {
      if (error) reject(error);
      resolve(body);
    });
  });
}

async function getCharacters (movieId) {
  const url = movieURL;

  try {
    const movie = await requestUrl(url);

    for (const charUrl of movie.characters) {
      const character = await requestUrl(charUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

getCharacters(movieId);
