#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

request(apiUrl, function(error, response, body) {
    if (error) {
        console.log(error)
        return
    }
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
        request(character, function (error, response, body) {
            if (error) {
                console.log(error);
                return
            }
            console.log(JSON.parse(body).name)
        })
    });
})
