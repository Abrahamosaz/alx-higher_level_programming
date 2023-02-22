$(function () {
  $('div#toggle_header').on('click', () => {
    if ($('header').hasClass('green') === true) {
      $('header').attr('class', 'red');
    } else {
      $('header').attr('class', 'green');
    }
  });
});
