#!/usr/bin/node
// Require the 'request' module for making HTTP requests
const request = require('request');

// Capture the movie ID passed as a command line argument
const movieId = process.argv[2];

// Construct the URL for the SWAPI API using the provided movie ID
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a GET request to the SWAPI API using the constructed URL
request(url, (err, response, body) => {
  // Check if an error occurred during the request
  if (err) {
    console.error(err); // Print the error message
    return; // Exit the function
  }

  // Parse the JSON data from the response body
  const data = JSON.parse(body);

  // Print the title of the movie from the parsed data
  console.log(`${data.title}`);
});
