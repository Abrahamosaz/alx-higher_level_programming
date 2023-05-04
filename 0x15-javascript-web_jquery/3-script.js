const $redHeader = $('div#red_header');
$(function () {
  $redHeader.click((event) => {
    $('header').addClass('red');
  });
});
