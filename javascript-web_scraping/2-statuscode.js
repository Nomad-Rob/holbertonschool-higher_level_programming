#!/usr/bin/node
// prints the status code of a GET request

// Store the command line argument (URL) in the myTargetURL variable
const myTargetURL = process.argv[2];

// Require the 'request' module for making HTTP requests
const request = require('request');

// Make a GET request to the provided URL
request(myTargetURL, 'GET', function (error, response, body) {
  // Check if an error occurred during the request
  if (error) {
    console.log('error:', error); // Print the error message
    return; // Exit the function
  }

  // Print the status code of the response
  console.log('code:', response.statusCode);
});
