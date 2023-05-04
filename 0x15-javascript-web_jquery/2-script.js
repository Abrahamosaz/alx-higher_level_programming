const $redHeader = $('div#red_header');
$(function () {
  $redHeader.click((event) => {
    $redHeader.css('color', '#FF0000');
  });
});
