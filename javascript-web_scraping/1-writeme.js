#!/usr/bin/node
// write a string to a file

// Require the 'fs' module for file reading and writing
const fileReader = require('fs');

// Capture the target file path and content from command line arguments
const myTargetFile = process.argv[2];
const myContent = process.argv[3];

// Use 'fs.writeFile' to write the content to the specified file
fileReader.writeFile(myTargetFile, myContent, 'utf8', function (err) {
  if (err) {
    console.log(err); // Log the error if writing fails
  }
});
