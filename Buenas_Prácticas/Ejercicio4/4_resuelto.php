<?php

$number = 5;

if (!filter_var($number, FILTER_VALIDATE_INT)) {
    echo "Error: number must be an integer.";
    exit(1);
}

$messages = [
    1 => "Number is 1",
    2 => "Number is 2",
    3 => "Number is 3",
    4 => "Number is 4",
    5 => "Bingo! Number is 5\nAnd 5*5 is " . ($number * $number)
];

if (isset($messages[$number])) {
    echo $messages[$number] . "\n";

    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";
    }
} else {
    echo "Error: Invalid number.";
    exit(1);

    exit;
}

?>
