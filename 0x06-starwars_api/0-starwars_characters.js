#!/usr/bin/node
const req = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

const getChar = (url) => new Promise((resolve, reject) =>
  req(url, (error, response, charBody) =>
    error || response.statusCode !== 200
      ? reject(error || response.statusCode)
      : resolve(JSON.parse(charBody).name)
  )
);

req(apiUrl, async (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const chars = await Promise.all(data.characters.map(getChar));
    chars.forEach((charName) => {
      console.log(charName);
    });
  } else {
    console.error(err || res.statusCode);
  }
});
