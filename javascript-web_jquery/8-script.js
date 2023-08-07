#!/usr/bin/node
// Get films from swapi.dev (but holberton)

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
// That was the 'but holberton' part, using their api over swapi.dev

$.get(url, function (data, textStatus) {
  for (const entry of data.results) {
    $('UL#list_movies').append('<li>' + entry.title + '</li>');
  }
});
