const redHeaderElement = $('#red_header');
const headerElement = $('header');

$(function () {
  $(redHeaderElement).on('click', () => {
    $(headerElement).addClass('red');
  });
});
