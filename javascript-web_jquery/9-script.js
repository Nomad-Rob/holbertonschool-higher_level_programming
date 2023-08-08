#!/usr/bin/node
// fetch Hello, from the headtag of the HTML

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

window.onload = function () {
  $.getJSON(url, function (data, status) {
    $('DIV#hello').text(data.hello);
  });
};

// also not working below 
// $(document).ready(function() {
    // Fetch the translation of "hello" from the provided URL
    //$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function(data) {
      // Extract the value of "hello" from the response
     // const helloValue = $(data).find('DIV#hello').text();
      
      // Set the extracted value as the content of DIV#hello
     //$('#hello').text(helloValue);
  //  });
  // });
