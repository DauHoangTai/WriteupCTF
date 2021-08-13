<?php
function check($payload) {
    for($i = 0; $i < strlen($payload); $i++)
        if(!(ord($payload[$i]) >= 32 && ord($payload[$i]) <= 125))
            return false;
    return true;
    }
?>