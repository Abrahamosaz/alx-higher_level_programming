const $redHeader = $('div#toggle_header');
const $setHeader = $('header');
$(function () {
  $redHeader.click((event) => {
    $setHeader.toggleClass('green red');
  });
});
