$(function () {
  $('div#add_item').click((event) => {
    $('ul.my_list').append('<li>Item</li>');
  });
});
