<?php

	function getData($file)
	{
		$j="{";
		$f=file_get_contents($file);
		$f1=explode("\n",$f);
		foreach($k as $f1)
		{
			$f2=explode(":",$f1);
			if((substr($f2[0],0,5) == 'https'))
			{
				$fret=getData($f2[1])
				$j=$j.$f2[0].":".$fret;
			}
			else
			{
				$j=$j.$f2[0].":".$f2[1];
			}
			$j=$j."}";
		}
		return $j;
	}
$m=getData("https://api.github.com/users/rashrag");	
echo $m;

?>