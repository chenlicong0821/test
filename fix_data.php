<?php

//问题股票代码,不包含前缀
$problemCode = 'BYSI';

//正确的前缀
$correctPrefix = 'oq';

//正确的股票类型，三级分类
$correctType = '010105';


//问题uin
$problemUin = 1161622;

//LIVE环境数据库连接
$link = mysqli_connect("172.16.1.11", "profileuser", "WgxGa_oieSm33sgqOnCD", "profile");

if (mysqli_connect_errno()) {
    printf("Connect failed: %s\r\n", mysqli_connect_error());
    exit();
}

if (mysqli_query($link, "set names utf8") === TRUE) {
}
else
{
    printf("set names failed\r\n");
    exit;
}

if ($result = mysqli_query($link, "SELECT * FROM portfolio where uin=" . $problemUin)) 
{
	$record = mysqli_fetch_assoc($result);
	if(empty($record['content']))
	{
				
    		printf("content empty\r\n");
		mysqli_free_result($result);
		exit;
	}

	$contentArr = json_decode($record['content'],true);
	if(empty($contentArr['portfolio']))
	{
    		printf("portfolio key empty\r\n");
		exit;
	}
	$finalResult = array();
	$finalProblemItem = array();
	//是否持仓了问题股票
	$isPosition = false;

	//自选列表中，是否存在问题股票
	$found = false;
	foreach($contentArr['portfolio'] as $item)
	{
		if($item['0'] == $problemCode )
		{
			$found = true;
			if($item['p'] == 1)
			{
				$isPosition = true;
			}
		}
		else
		{
			$finalResult[] = $item;
		}
	}

	if($found)
	{
		//如果找到了问题股票
		if($isPosition)
		{
			$finalProblemItem = array('0'=>$problemCode,'100'=>$correctPrefix,'stock_type'=>$correctType,'p'=>1);
		}
		else
		{
			$finalProblemItem = array('0'=>$problemCode,'100'=>$correctPrefix,'stock_type'=>$correctType,'p'=>0);
		}
		array_unshift($finalResult, $finalProblemItem);
		$updateContent = json_encode(array('portfolio'=>$finalResult));



		$updateSql = 'update portfolio set content=' .  '\'' . $updateContent .  '\''. ' where uin=' . $problemUin;
		$updateResult = mysqli_query($link, $updateSql);
		if($updateResult)
		{
			var_dump("修复成功");
		}
		else
		{
			var_dump("修复失败");
		}
	}
	else
	{
	
		var_dump("该用户的自选列表中没有问题股票" . $problemCode);
		exit;
	}
}
else
{
    printf("select failed\n");
    exit;
}

