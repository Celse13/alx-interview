#!/usr/bin/node
const request = require('request');
const apiUrl = `https://swapi.dev/api/films/${process.argv[2]}`;

const getChar = (url) => new Promise((resolve, reject) =>
  request(url, (error, response, charBody) => {
    if (error || response.statusCode !== 200) {
      reject(error || `Response status: ${response.statusCode}`);
    } else {
      resolve(JSON.parse(charBody).name);
    }
  })
);

request(apiUrl, async (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    try {
      const chars = await Promise.all(data.characters.map(getChar));
      chars.forEach((charName) => {
        console.log(charName);
      });
    } catch (error) {
      console.error(`Error getting character names: ${error}`);
    }
  } else {
    console.error(err || `Response status: ${res.statusCode}`);
  }
});
