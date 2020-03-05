<?php
    if(isset($_POST['img'])) {
        $args = [];
        for($n = 0; $n < count($_POST['img']); $n++) {
            $args[$n] = implode(",", $_POST['img'][$n]);
        }
        $arg = implode(";", $args);
        var_dump(@ini_get("disable_functions"));
        $output = "";
        $output = system('C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37\\python.exe C:\\xampp\\htdocs\\sic\\python\\bezier_fit.py '.$arg." 2>&1", $output);
        #echo explode('CB', $output)[1];
    } else {
        echo 'X';
    }
?>