#!/usr/bin/node

const request = require('request');

const movieIdInput = process.argv[2];
const filmEndPointUrl = 'https://swapi-api.hbtn.io/api/films/' + movieIdInput;
let characters = [];
const characterNames = [];

const fetchCharacters = async () => {
  return new Promise((resolve, reject) => {
    request(filmEndPointUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        console.error('Error: ', error, '| StatusCode: ', response.statusCode);
        reject('Failed to fetch film data'); // Reject the promise with an error message
      } else {
        const filmData = JSON.parse(body);
        characters = filmData.characters;
        resolve();
      }
    });
  });
};

const fetchCharacterNames = async () => {
  if (characters.length > 0) {
    for (const characterUrl of characters) {
      await new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error || response.statusCode !== 200) {
            console.error('Error: ', error, '| StatusCode: ', response.statusCode);
            reject('Failed to fetch character data'); // Reject the promise with an error message
          } else {
            const characterData = JSON.parse(body);
            characterNames.push(characterData.name);
            resolve();
          }
        });
      });
    }
  } else {
    console.error('Error: No characters were fetched !');
  }
};

const displayCharacterNames = async () => {
  try {
    await fetchCharacters();
    await fetchCharacterNames();

    for (const name of characterNames) {
      if (name === characterNames[characterNames.length - 1]) {
        process.stdout.write(name);
      } else {
        process.stdout.write(name + '\n');
      }
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

displayCharacterNames();
