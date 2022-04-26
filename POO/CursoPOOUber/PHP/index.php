<?php
require_once('car.php');
require_once('ubeX.php');
require_once('account.php');

$uberX = new UberX("AWS123",new Account("Andres Herrera","50202354"), "Chevrolet", "Spark");
$uberX->printDataCar();

>