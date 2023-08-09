#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('API Error:', response.statusCode, response.statusMessage);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    process.exit(0);
  }

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Character Error:', charError);
      } else if (charResponse.statusCode !== 200) {
        console.error('Character API Error:', charResponse.statusCode, charResponse.statusMessage);
      } else {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      }
    });
  });
});

