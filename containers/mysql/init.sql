-- MYSQL_USERに権限を付与
GRANT ALL PRIVILEGES ON *.* TO 'django'@'%';
FLUSH PRIVILEGES;
