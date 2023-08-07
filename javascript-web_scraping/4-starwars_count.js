#!/usr/bin/node
// prints the movie title

// Capture the target URL passed as a command line argument
const myTargetURL = process.argv[2];

// Require the 'request' module for making HTTP requests
const request = require('request');

// Define the data for the request, including URL, method, and headers
const requestData = {
  url: myTargetURL,
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
};

// Make a GET request to the specified URL using the defined request data
request(requestData, function (error, response, body) {
  // Check if an error occurred during the request
  if (error) {
    console.log('error:', error); // Print the error message
    return; // Exit the function
  }

  // Parse the JSON data from the response body and extract 'results'
  const films = JSON.parse(body).results;

  // Initialize a counter for characters containing '18'
  let charCount = 0;

  // Iterate through each film's characters and count those containing '18'
  for (const film of films) {
    for (const char of film.characters) {
      if (char.includes('18')) {
        charCount++;
      }
    }
  }

  // Print the total count of characters containing '18'
  console.log(charCount);
});
