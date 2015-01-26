<?

$aResult = array(
    'playlist' => array(
        '1' => array(
            'src' => 'songs/Mark/Mark.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 1', 'poster' => ''
            ),
        ),    
        '2' => array(
            'src' => 'songs/Mark/Mark2.mp3', 'type' => 'audio/mp3',
            'config' => array(
                'title' => 'Song 2', 'poster' => ''
            ),

        ),
    ),
);

header("Content-Type: application/json");
require_once('Services_JSON.php');
$oJson = new Services_JSON();
echo $oJson->encode($aResult);

?>