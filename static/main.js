$(document).ready(function() {
    $('.small_player').speakker({
        file: 'data/01.mp3',
        poster: 'data/cover.png',
        title: 'Song #1',
        theme: 'dark'
    });
    $().speakker({
        file: 'playlist.php',
        playlist: true,
        theme: 'dark',
    });
});
