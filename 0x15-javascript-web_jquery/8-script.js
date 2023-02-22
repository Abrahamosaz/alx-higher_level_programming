$(function () {
  const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  const listMovies = $('ul#list_movies');
  $.get(URL, function (data, textStatus) {
    if (textStatus === 'success') {
      const resultArray = data.results;
      for (let i = 0; i < resultArray.length; i++) {
        $(listMovies).append('<li>' + resultArray[i].title + '</li>');
      }
    }
  });
});
