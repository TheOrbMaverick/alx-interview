#!/usr/local/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  };

  const characterPromises = characters.map((url) => fetchCharacterName(url));

  Promise.all(characterPromises)
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((error) => console.error(error));
});