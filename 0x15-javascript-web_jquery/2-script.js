const headerElement = $('#red_header');
$(function () {
  $(headerElement).on('click', () => {
    $(headerElement).css('color', '#FF0000');
  });
});
