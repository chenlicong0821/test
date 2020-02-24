
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_many_user`(IN start INT(10), IN max_num INT(10))
BEGIN
DECLARE i INT DEFAULT 0;
DECLARE date_start DATETIME DEFAULT ('2017-01-01 00:00:00');
DECLARE date_temp DATETIME;
SET date_temp = date_start;
SET autocommit=0;
REPEAT
SET i=i+1;
SET date_temp = date_add(date_temp, interval RAND()*60 second);
INSERT INTO user(user_id, user_name, create_time)
VALUES((start+i), CONCAT('user_',i), date_temp);
UNTIL i = max_num
END REPEAT;
COMMIT;
END


CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_many_product_comments`(IN START INT(10), IN max_num INT(10))
BEGIN
DECLARE i INT DEFAULT 0;
DECLARE date_start DATETIME DEFAULT ('2018-01-01 00:00:00');
DECLARE date_temp DATETIME;
DECLARE comment_text VARCHAR(25);
DECLARE user_id INT;
SET date_temp = date_start;
SET autocommit=0;
REPEAT
SET i=i+1;
SET date_temp = date_add(date_temp, INTERVAL RAND()*60 SECOND);
SET comment_text = substr(MD5(RAND()),1, 20);
SET user_id = FLOOR(RAND()*1000000);
INSERT INTO product_comment(comment_id, product_id, comment_text, comment_time, user_id)
VALUES((START+i), 10001, comment_text, date_temp, user_id);
UNTIL i = max_num
END REPEAT;
COMMIT;
END