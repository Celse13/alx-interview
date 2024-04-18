#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function getUrl (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, resonse, body) => {
      if (error) reject(error);
      resolve(body);
    });
  });
}

async function getCharacters (movieId) {
  try {
    const movie = await getUrl(url);

    for (const getUrl of movie.characters) {
      const character = await getUrl(getUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

getCharacters(movieId);
