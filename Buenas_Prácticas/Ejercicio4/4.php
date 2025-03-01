<?php
//CWE-398: Indicator of Poor Code Quality
//CWE-710: Improper Adherence to Coding Standards
$number = 5;
$string = strval($number); //CWE-704: Incorrect Type Conversion or Cast
if (str_contains($string, '1')) { //CWE-682: Incorrect Calculation
    echo "Number is 1\n";
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";}}
if (str_contains($string, '2')) {
    echo "Number is 2\n";
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";}}
if (str_contains($string, '3')) {
    echo "Number is 3\n";
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";}}
if (str_contains($string, '4')) {
    echo "Number is 4\n";
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";}}
if (str_contains($string, '5')) {
    echo "Bingo! Number is 5\n";
	echo "And 5*5 is ";
    // CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')
    // CWE-676: Use of Potentially Dangerous Function
    //CWE-1079: Improper Separation of Concerns in Code
	eval('echo ' . ($number * $number) . ';'); 
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";}}
?>
