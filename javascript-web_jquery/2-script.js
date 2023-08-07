#!/usr/bin/node
// Update color of <header> tag to red, using JQUERY

$('div#red_header').click(
  function () {
    $('header').css('color', '#FF0000');
  }
);
