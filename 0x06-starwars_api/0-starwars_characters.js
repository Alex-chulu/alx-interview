#!/usr/bin/node

const fs = require('fs');
const axios = require('axios');

function getCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  axios.get(apiUrl)
    .then(response => {
      const filmData = response.data;
      const characterUrls = filmData.characters;

      characterUrls.forEach(characterUrl => {
        axios.get(characterUrl)
          .then(characterResponse => {
            const characterData = characterResponse.data;
            console.log(characterData.name);
          })
          .catch(error => {
            console.error(`Failed to fetch character data: ${error.response.status}`);
          });
      });
    })
    .catch(error => {
      console.error(`Failed to fetch film data: ${error.response.status}`);
    });
}

if (process.argv.length !== 3) {
  console.error("Usage: node script.js <movie_id>");
  process.exit(1);
}

const movieId = process.argv[2];
getCharacters(movieId);
