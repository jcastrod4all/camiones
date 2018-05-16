<?php
require_once "models/connection.php";

header('Content-Type: application/json');

class Data {
    public function dataChart () {
        $stmt = Connection::connect()->prepare("SELECT id, reg_date FROM count_passengers");
        $stmt->execute();

        $data = $stmt->fetchAll(\PDO::FETCH_ASSOC);

        print json_encode($data);

        return $data;
        $stmt->close();
    }
}

$dataChart = new Data();
$dataChart -> dataChart();