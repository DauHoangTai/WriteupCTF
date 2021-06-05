<?php
class CalcModel
{
    public static function getCalc($formula)
    {
        if (strlen($formula) >= 100 || preg_match_all('/[a-z\'"]+/i', $formula)) {
            return '🤡 dont bite the hand that feeds you human 🤡';
        }
        try {
            eval('$pcalc = ' . $formula . ';');
            return isset($pcalc) ? $pcalc : '?';
        }
        catch (ParseError $err) {
           return '🚨 report to the nearest galactic federation agency 🚨';
        }  
    }
}