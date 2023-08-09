#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

const baseUrl = 'https://swapi.dev/api/films/';

request(baseUrl + movieId, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
      } else {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
});
