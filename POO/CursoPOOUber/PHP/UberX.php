<?php
require_once('car.php');
class UberX extends Car{
    public $brand;
    public $model;

    function __construct($license,$driver,$brand, $model){
        parent::__construct($license, $driver);
        $this->brand = $brand;
        $this->model = $model;
    }
}

>