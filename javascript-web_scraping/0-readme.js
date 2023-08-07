#!/usr/bin/node
// Read and print the content of a file

// Require the 'fs' module for file reading
const fileReader = require('fs');

// Capture the target file path from command line arguments
const myTargetFile = process.argv[2];

// Use 'fs.readFile' to read the content of the specified file
fileReader.readFile(myTargetFile, 'utf8', function (err, data) {
  if (err) {
    console.log(err); // Log the error if reading fails
  } else {
    console.log(data); // Log the content of the file if reading is successful
  }
});
