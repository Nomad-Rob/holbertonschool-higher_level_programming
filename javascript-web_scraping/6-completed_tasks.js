#!/usr/bin/node
// Save the contents of a webpage to a file

// Capture the target URL from command line arguments,
// or use a default URL if no argument is provided
const myTargetURL = process.argv[2] || 'https://jsonplaceholder.typicode.com/todos';

// Require the 'request' module for making HTTP requests
const request = require('request');

// Define the data for the request
const requestData = {
  url: myTargetURL,
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
};

// Use the 'request' module to make an HTTP GET request
request(requestData, 'GET', function (error, response, body) {
  if (error) {
    console.log('error:', error); // Log the error if request fails
    return;
  }

  const results = {}; // Initialize an object to store results
  const data = JSON.parse(body); // Parse the JSON response
  for (const task of data) {
    if (task.completed) {
      // Count completed tasks for each user
      results[task.userId] = (results[task.userId] + 1) || 1;
    }
  }

  console.log(results); // Log the results object containing completed tasks by user
});
