#!/usr/bin/node
// Save the contents of a webpage to a file

// Capture the target URL and file name from command line arguments (or use defaults)
const myTargetURL = process.argv[2] || 'http://loripsum.net/api';
const fileName = process.argv[3] || 'fetched';

// Require the 'request' module for making HTTP requests
const request = require('request');

// Define the data for the request, including URL and method
const requestData = {
  url: myTargetURL,
  method: 'GET'
};

// Function to write contents to a file
function WriteToFile (file, contents) {
  const fileSystem = require('fs');
  fileSystem.writeFile(file, contents, 'utf8', function (err) {
    if (err) {
      console.log(err); // Log the error if writing fails
    }
  });
}

// Make a GET request to the specified URL using the defined request data
request(requestData, function (error, response, body) {
  // Check if an error occurred during the request
  if (error) {
    console.log('error:', error); // Print the error message
    return; // Exit the function
  }

  // Call the WriteToFile function to save the response body to the specified file
  WriteToFile(fileName, body);
});
