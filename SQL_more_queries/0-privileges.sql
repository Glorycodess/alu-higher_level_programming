-- Correct output: user_0d_1 root user
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Correct output: user_0d_2 SELECT and INSERT privileges on the database user_2_db
SHOW GRANTS FOR 'user_0d_2'@'localhost';
