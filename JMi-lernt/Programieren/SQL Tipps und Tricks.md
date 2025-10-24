# Nicht vergessen

mydb.commit()
mydb.close()
# Namen
- keine - in Tabellennamen
	- wenn doch dann `backticks` verwenden 

https://docs.metasploit.com/api/Msf/Exploit/Remote/HTTP.html

gegen sql injection. Kein Werte direkt aus Eingabe übernehmen und in ein insert schreiben. statt desen Platzhalte in values %s und Liste der WErte
insert into tabelle(col 1, col 2)values(%s, %s)wert1,wert2;

# Fremdschlüssel stehen geblieben
Mit
`   [SELECT](http://localhost/phpmyadmin/url.php?url=https://dev.mysql.com/doc/refman/8.0/en/select.html) RefCons.constraint_schema, RefCons.table_name, RefCons.referenced_table_name, RefCons.constraint_name, KeyCol.column_name FROM information_schema.referential_constraints RefCons JOIN information_schema.key_column_usage KeyCol ON RefCons.constraint_schema = KeyCol.table_schema [AND](http://localhost/phpmyadmin/url.php?url=https://dev.mysql.com/doc/refman/8.0/en/logical-operators.html%23operator_and) RefCons.table_name = KeyCol.table_name [AND](http://localhost/phpmyadmin/url.php?url=https://dev.mysql.com/doc/refman/8.0/en/logical-operators.html%23operator_and) RefCons.constraint_name = KeyCol.constraint_name WHERE RefCons.constraint_schema = 'Name_Datenbank';   `

kann ich überprüfen welche constraint gesetzt sind. Das ist wichtig wenn ein foren Key ins leere zeigt. Dann den constrain droppen um die collumn löschen zu können.

