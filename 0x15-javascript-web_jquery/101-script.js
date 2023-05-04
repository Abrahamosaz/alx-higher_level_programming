$(function () {
  $('div#add_item').click((event) => {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click((event) => {
    const list = $('ul.my_list li');
    if (list.length > 0) {
      list[list.length - 1].remove();
    }
  });
  $('div#clear_list').click((event) => {
    $('ul.my_list').empty();
  });
});
