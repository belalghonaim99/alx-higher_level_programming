#!/usr/bin/node
//prints the number of movies where the character “Wedge Antilles”
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const movies = JSON.parse(body).movies;
    const cwwa = movies.reduce((count, movie) => {
      return movie.characters.some((character) => character.endsWith('/18/')) 
      ? count + 1 : count;
    }, 0);

    console.log(cwwa);
  } else {
    console.error(error);
  }
});
