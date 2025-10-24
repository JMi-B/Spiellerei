```
myisamchk --recover tbl
myisamchk --save-recover tbl
``` ```
mysqld_safe --skip-grant-tables
``` [mysqld]  
skip-grant-tables `repair table 'table_name' use_frm`

`mysqld]
datadir=c:/xampp/mysql/data
skip-grant-tables
[client]`


Für den Fehler #1030 - Fehler 176 "Read page with wrong checksum" von Speicher-Engine Aria 
Beim Versuch Rechte zu vergeben

```

```
cd C:\xampp\mysql\bin
mysqlcheck -A -u root -r