<?

$aResult = array(
    'playlist' => array(
        '1' => array(
            'src' => 'data/01.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 1', 'poster' => 'data/cover.png'
            ),
        ),
        '2' => array(
            'src' => 'data/02.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 2', 'poster' => 'data/cover.png'
            ),
        ),
        '3' => array(
            'src' => 'data/03.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 3', 'poster' => 'data/cover.png'
            ),
        ),
        '4' => array(
            'src' => 'data/04.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 4', 'poster' => 'data/cover.png'
            ),
        ),
        '5' => array(
            'src' => 'data/05.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 5', 'poster' => 'data/cover.png'
            ),
        ),
        '6' => array(
            'src' => 'data/06.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 6', 'poster' => 'data/cover.png'
            ),
        ),
        '7' => array(
            'src' => 'data/07.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 7', 'poster' => 'data/cover.png'
            ),
        ),
        '8' => array(
            'src' => 'data/08.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 8', 'poster' => 'data/cover.png'
            ),
        ),
    )
);

header("Content-Type: application/json");
require_once('Services_JSON.php');
$oJson = new Services_JSON();
echo $oJson->encode($aResult);

?>