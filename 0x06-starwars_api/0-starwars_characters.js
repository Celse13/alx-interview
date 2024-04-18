#!/usr/bin/node
import request from 'request';
import util from 'util';

const requestPromise = util.promisify(request);

async function getCharacterName (url) {
  try {
    const response = await requestPromise(url);
    return JSON.parse(response.body).name;
  } catch (error) {
    console.error(error);
  }
}

async function printCharacters (movieId) {
  try {
    const response = await requestPromise(`https://swapi.dev/api/films/${movieId}/`);
    const body = JSON.parse(response.body);
    const characters = body.characters;
    for (const character of characters) {
      const name = await getCharacterName(character);
      console.log(name);
    }
  } catch (error) {
    console.error(error);
  }
}

const movieId = process.argv[2];
printCharacters(movieId);
