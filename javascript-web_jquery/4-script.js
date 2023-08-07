#!/usr/bin/node
// Update class of <header> tag to red, using JQUERY

let isred = $('header').hasClass('red');

$('div#toggle_header').click(
  function () {
    if (isred) {
      $('header').removeClass('red');
      $('header').addClass('green');
    } else {
      $('header').removeClass('green');
      $('header').addClass('red');
    }
    isred = !isred;
  }
);
