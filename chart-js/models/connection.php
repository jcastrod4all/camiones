<?php

class Connection {

    public function connect() {

        $link = new PDO("mysql:host=localhost;dbname=camiones", "root", "");
        return $link;
    }
}