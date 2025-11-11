#sql #select #join 
Von Georg
# Spezielle `Select` Befehle
## Group by
``GROUPBY

``SELECT genre, COUNT(*) AS number_of_movies  
``FROM Movies  
``GROUP BY genre;

``SELECT genre, COUNT(*) AS number_of_movies  
``FROM Movies  
``GROUP BY genre  
``HAVING COUNT(*) > 2;

## Order by
``ORDERBY

``SELECT movie_id, title, year, genre  
``FROM Movies  
``ORDER BY year ASC, title ASC;

``SELECT m.title, m.year, a.name, ma.role   
``FROM MovieActors ma, Movies m, Actors a   
``WHERE ma.movie_id = m.movie_id AND ma.actor_id = a.actor_id;

## Join
### Inner Join
``INNER JOIN  
Alle Filme mit Schauspielern und Rollen abfragen. Zeigt nur Filme, die auch Schauspieler in der Liste haben

Nur Matches in beiden Tabellen

``SELECT m.title, m.year, a.name, ma.role  
``FROM MovieActors ma  
``JOIN Movies m ON ma.movie_id = m.movie_id  
``JOIN Actors a ON ma.actor_id = a.actor_id;

### Left Join
``LEFT JOIN  
Zeigt alle Filme, auch die, die keine Schauspieler eingetragen haben

Alle Einträge der linken Tabelle, mit zugehörigen Daten aus der rechten Tabelle

``SELECT m.title, ma.role, a.name  
``FROM Movies m  
``LEFT JOIN MovieActors ma ON m.movie_id = ma.movie_id  
``LEFT JOIN Actors a ON ma.actor_id = a.actor_id;

### Right Outer Join
``RIGHT OUTER JOIN

Alle Filme und Rollen, an denen ein Schauspieler teilgenommen hat

Alle Reihen der rechten Tabelle, mit zugehörigen Daten aus der linken Tabelle

``SELECT  
    ``a.actor_id,  
    ``a.name AS actor_name,  
    ``m.title AS movie_title,  
    ``ma.role  
``FROM  
    ``Movies m  
    ``RIGHT JOIN MovieActors ma ON m.movie_id = ma.movie_id  
    ``RIGHT JOIN Actors a ON ma.actor_id = a.actor_id;  
## Standatabweichung
``STDDEV

``SELECT STDDEV(year) AS ReleaseYearStdDev  
``FROM Movies;
## Tabellen und Daten
### Die Tabellen, die ich gerade genutzt habe:

``CREATE TABLE Movies (  
    ``movie_id INTEGER PRIMARY KEY,  
    ``title TEXT,  
    ``year INTEGER,  
    ``genre TEXT  
``);

``CREATE TABLE Actors (  
    ``actor_id INTEGER PRIMARY KEY,  
    ``name TEXT  
``);

``CREATE TABLE MovieActors (  
    ``movie_id INTEGER,  
    ``actor_id INTEGER,  
    ``role TEXT,  
    ``FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),  
    ``FOREIGN KEY (actor_id) REFERENCES Actors(actor_id)  
``);

### Und die Daten:

``INSERT INTO Movies (movie_id, title, year, genre) VALUES (1, 'Inception', 1996, 'Sci-Fi');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (2, 'Forrest Gump', 1982, 'Drama');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (3, 'The Matrix', 1984, 'Action');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (4, 'Pulp Fiction', 1995, 'Crime');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (5, 'Fight Club', 2018, 'Thriller');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (6, 'Interstellar', 2012, 'Adventure');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (7, 'The Godfather', 1980, 'Animation');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (8, 'The Dark Knight', 2000, 'Fantasy');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (9, 'Gladiator', 1989, 'History');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (10, 'Avatar', 1998, 'Comedy');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (11, 'Titanic', 2008, 'War');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (12, 'Memento', 1993, 'Romance');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (13, 'Shrek', 2003, 'Mystery');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (14, 'Toy Story', 1997, 'Family');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (15, 'Alien', 1991, 'Horror');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (16, 'Goodfellas', 2004, 'Biography');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (17, 'Saving Private Ryan', 1992, 'Sport');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (18, 'Jurassic Park', 1988, 'Musical');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (19, 'Braveheart', 1983, 'Western');  
``INSERT INTO Movies (movie_id, title, year, genre) VALUES (20, 'Heat', 1981, 'Documentary');

``INSERT INTO Actors (actor_id, name) VALUES (1, 'Leonardo DiCaprio');  
``INSERT INTO Actors (actor_id, name) VALUES (2, 'Tom Hanks');  
``INSERT INTO Actors (actor_id, name) VALUES (3, 'Keanu Reeves');  
``INSERT INTO Actors (actor_id, name) VALUES (4, 'Carrie-Anne Moss');  
``INSERT INTO Actors (actor_id, name) VALUES (5, 'Brad Pitt');  
``INSERT INTO Actors (actor_id, name) VALUES (6, 'Morgan Freeman');  
``INSERT INTO Actors (actor_id, name) VALUES (7, 'Robert De Niro');  
``INSERT INTO Actors (actor_id, name) VALUES (8, 'Natalie Portman');  
``INSERT INTO Actors (actor_id, name) VALUES (9, 'Robin Williams');  
``INSERT INTO Actors (actor_id, name) VALUES (10, 'Angelina Jolie');  
``INSERT INTO Actors (actor_id, name) VALUES (11, 'Johnny Depp');  
``INSERT INTO Actors (actor_id, name) VALUES (12, 'Kate Winslet');  
``INSERT INTO Actors (actor_id, name) VALUES (13, 'Emma Stone');  
``INSERT INTO Actors (actor_id, name) VALUES (14, 'Will Smith');  
``INSERT INTO Actors (actor_id, name) VALUES (15, 'Sandra Bullock');  
``INSERT INTO Actors (actor_id, name) VALUES (16, 'Matt Damon');  
``INSERT INTO Actors (actor_id, name) VALUES (17, 'Samuel L. Jackson');  
``INSERT INTO Actors (actor_id, name) VALUES (18, 'Julia Roberts');  
``INSERT INTO Actors (actor_id, name) VALUES (19, 'Chris Hemsworth');  
``INSERT INTO Actors (actor_id, name) VALUES (20, 'Scarlett Johansson');

``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (11, 9, 'Cobb');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (2, 18, 'Forrest Gump');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (6, 14, 'Neo');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (2, 10, 'Trinity');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (17, 1, 'Tyler Durden');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (17, 17, 'Red');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (19, 10, 'Don Vito');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (6, 12, 'Joker');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (13, 18, 'Maximus');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (15, 19, 'Jake Sully');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (13, 9, 'Jack Dawson');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (10, 13, 'Leonard');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (18, 8, 'Shrek');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (15, 19, 'Woody');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (7, 14, 'Ripley');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (20, 19, 'Tommy');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (10, 17, 'Captain Miller');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (3, 1, 'Grant');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (8, 1, 'Wallace');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (14, 12, 'McCauley');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (11, 10, 'Bonus Role');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (10, 9, 'Dr. Jones');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (1, 4, 'Agent Smith');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (9, 7, 'Mickey');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (14, 18, 'Elsa');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (9, 10, 'Buzz');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (18, 2, 'Andy');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (15, 9, 'Belle');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (13, 19, 'Napoleon');  
``INSERT INTO MovieActors (movie_id, actor_id, role) VALUES (2, 7, 'Frodo');
# Weitere Aufgaben
Hi,

  ![[soccer.sql]]

Zur Vertiefung des Themas gestern mit den SQL JOINs habe ich nochmal eine Beispiel-Datenbank vorbereitet. Um die verschiedenen JOINs auszuprobieren, sind hier ein paar Aufgaben.

  

## 1. Erstelle ein Query, dass für jeden Spieler das Team anzeigt. (24 Ergebnisse)
`SELECT p.player_name, t.team_name
	`` FROM players p, teams t 
	``WHERE p.team_id=t.team_id;`

|[player_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=players&sql_query=SELECT+p.player_name%2C+t.team_name+%0D%0AFROM+players+p%2C+teams+t+%0D%0AWHERE+p.team_id%3Dt.team_id++%0AORDER+BY+%60p%60.%60player_name%60+ASC&sql_signature=a34d14c5bc32a81988efa874f583f4fc67ea76b166fbaeaa3fbc973cc3f15312&session_max_rows=25&is_browse_distinct=0)|[team_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=players&sql_query=SELECT+p.player_name%2C+t.team_name+%0D%0AFROM+players+p%2C+teams+t+%0D%0AWHERE+p.team_id%3Dt.team_id++%0AORDER+BY+%60t%60.%60team_name%60+ASC&sql_signature=9903607c2d65f4940e5754040ec694de2f813d1a41cc7bff1338784cbfbf6634&session_max_rows=25&is_browse_distinct=0)||
|---|---|---|
|Alice|Red Lions|
|Bob|Red Lions|
|Uma|Red Lions|
|Wendy|Red Lions|
|Charlie|Blue Sharks|
|David|Blue Sharks|
|Victor|Blue Sharks|
|Xander|Blue Sharks|
|Eve|Green Eagles|
|Frank|Green Eagles|
|Grace|Yellow Tigers|
|Hank|Yellow Tigers|
|Ivy|Black Panthers|
|Jack|Black Panthers|
|Kate|White Wolves|
|Leo|White Wolves|
|Mia|Orange Foxes|
|Ned|Orange Foxes|
|Olivia|Silver Bulls|
|Paul|Silver Bulls|
|Quinn|Golden Hawks|
|Rachel|Golden Hawks|
|Sam|Purple Snakes|
|Tina|Purple Snakes|

## 2. Erstelle ein Query, dass für jedes Spiel das Datum und das Heim-Team anzeigt. (12 Ergebnisse)

``SELECT m.match_date, t.team_name
``FROM matches m, teams t
``WHERE m.home_team_id=t.team_id;

|[match_date](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=m&sql_query=SELECT+m.match_date%2C+t.team_name%0D%0AFROM+matches+m%2C+teams+t%0D%0AWHERE+m.home_team_id%3Dt.team_id++%0AORDER+BY+%60m%60.%60match_date%60+DESC&sql_signature=e9d85497165ab333728860560d699ead1d5d70edcaf594957a19eb55c71298da&session_max_rows=25&is_browse_distinct=0)|[team_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=m&sql_query=SELECT+m.match_date%2C+t.team_name%0D%0AFROM+matches+m%2C+teams+t%0D%0AWHERE+m.home_team_id%3Dt.team_id++%0AORDER+BY+%60t%60.%60team_name%60+ASC&sql_signature=77336dc3b70b57cd740bea53920d643f36e25cda2344331b283dd06f35bce633&session_max_rows=25&is_browse_distinct=0)||
|---|---|---|
|2025-11-01|Red Lions|
|2025-11-02|Blue Sharks|
|2025-11-03|Green Eagles|
|2025-11-04|Yellow Tigers|
|2025-11-05|Black Panthers|
|2025-11-06|White Wolves|
|2025-11-07|Orange Foxes|
|2025-11-08|Silver Bulls|
|2025-11-09|Golden Hawks|
|2025-11-10|Purple Snakes|
|2025-11-11|Red Lions|
|2025-11-12|Blue Sharks|

## 3. Erstelle ein Query, dass für Spiel 5 das Datum, die Namen aller Spieler, die teilgenommen haben, und den Team-Namen der Spieler anzeigt. (2 Ergebnisse)
### Annährung
`select p.player_name, t.team_name, m.match_date
``from matches m, players p, teams t 
``where m.match_id = 5;

ergibt

|[player_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=p&sql_query=select+p.player_name%2C+t.team_name%2C+m.match_date%0D%0Afrom+matches+m%2C+players+p%2C+teams+t+%0D%0Awhere+m.match_id+%3D+5++%0AORDER+BY+%60p%60.%60player_name%60+ASC&sql_signature=913706c8ffa82de53f9eb8b43cb933b1739471908ac58ea07d6772577d6400b2&session_max_rows=25&is_browse_distinct=0)|[team_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=p&sql_query=select+p.player_name%2C+t.team_name%2C+m.match_date%0D%0Afrom+matches+m%2C+players+p%2C+teams+t+%0D%0Awhere+m.match_id+%3D+5++%0AORDER+BY+%60t%60.%60team_name%60+ASC&sql_signature=01798fe05a86dafcfcc0bb8accdec76fac313bb898d57e01550b432706dda642&session_max_rows=25&is_browse_distinct=0)|[match_date](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=p&sql_query=select+p.player_name%2C+t.team_name%2C+m.match_date%0D%0Afrom+matches+m%2C+players+p%2C+teams+t+%0D%0Awhere+m.match_id+%3D+5++%0AORDER+BY+%60m%60.%60match_date%60+DESC&sql_signature=7d3ec93d14c4a25c379f00f6f2cd4d2d4caf7a34a673d365d940560555fe21fb&session_max_rows=25&is_browse_distinct=0)||
|---|---|---|---|
|Alice|Red Lions|2025-11-05|
|Alice|Blue Sharks|2025-11-05|
|Alice|Green Eagles|2025-11-05|
|Alice|Yellow Tigers|2025-11-05|
|Alice|Black Panthers|2025-11-05|
|Alice|White Wolves|2025-11-05|
|Alice|Orange Foxes|2025-11-05|
|Alice|Silver Bulls|2025-11-05|
|Alice|Golden Hawks|2025-11-05|
|Alice|Purple Snakes|2025-11-05|
|Alice|Pink Dolphins|2025-11-05|
|Alice|Brown Bears|2025-11-05|
|Bob|Red Lions|2025-11-05|
|Bob|Blue Sharks|2025-11-05|
|Bob|Green Eagles|2025-11-05|
|Bob|Yellow Tigers|2025-11-05|
|Bob|Black Panthers|2025-11-05|
|Bob|White Wolves|2025-11-05|
|Bob|Orange Foxes|2025-11-05|
|Bob|Silver Bulls|2025-11-05|
|Bob|Golden Hawks|2025-11-05|
|Bob|Purple Snakes|2025-11-05|
|Bob|Pink Dolphins|2025-11-05|
|Bob|Brown Bears|2025-11-05|
|Charlie|Red Lions|2025-11-05|

Alle Teamnamen für drei Spieler
in der Tabelle `player_matches` stehen für Spiel 5 `player_id` 9 und 10, das sind Ivy und Jack. Beide sind in team 5 Black Panthers
`matches` gibt die Teams über die `home_team_id` und `away_team_id ` an
`matches_players` gibt für die `match_id` die `player_id`
Jeder Spieler hat eine `team_id`
### 2. Annährung
``select p.player_name, t.team_name, m.match_date
``from matches m, players p, teams t, player_matches pm
``where m.match_id = 5 
``AND pm.player_id = p.player_id
``AND p.team_id =t.team_id;

ergibt
|[player_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=p&sql_query=select+p.player_name%2C+t.team_name%2C+m.match_date%0D%0Afrom+matches+m%2C+players+p%2C+teams+t%2C+player_matches+pm%0D%0Awhere+m.match_id+%3D+5+%0D%0AAND+pm.player_id+%3D+p.player_id%0D%0AAND+p.team_id+%3Dt.team_id++%0AORDER+BY+%60p%60.%60player_name%60+ASC&sql_signature=dbc794818fbc5dfc37ea25c5c5ae8e2b32b01746b5ebec08464cf4ee7fb14e04&session_max_rows=25&is_browse_distinct=0)|[team_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=p&sql_query=select+p.player_name%2C+t.team_name%2C+m.match_date%0D%0Afrom+matches+m%2C+players+p%2C+teams+t%2C+player_matches+pm%0D%0Awhere+m.match_id+%3D+5+%0D%0AAND+pm.player_id+%3D+p.player_id%0D%0AAND+p.team_id+%3Dt.team_id++%0AORDER+BY+%60t%60.%60team_name%60+ASC&sql_signature=e902d0939ee1990f35b4f2110f7ef6d3763ac8c790324265eb1696f5540b2db9&session_max_rows=25&is_browse_distinct=0)|[match_date](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=p&sql_query=select+p.player_name%2C+t.team_name%2C+m.match_date%0D%0Afrom+matches+m%2C+players+p%2C+teams+t%2C+player_matches+pm%0D%0Awhere+m.match_id+%3D+5+%0D%0AAND+pm.player_id+%3D+p.player_id%0D%0AAND+p.team_id+%3Dt.team_id++%0AORDER+BY+%60m%60.%60match_date%60+DESC&sql_signature=cba040f69845d391f9bea1d35275323d96f41a64ca474400366d248736dd856f&session_max_rows=25&is_browse_distinct=0)||
|---|---|---|---|
|Alice|Red Lions|2025-11-05|
|Bob|Red Lions|2025-11-05|
|Uma|Red Lions|2025-11-05|
|Wendy|Red Lions|2025-11-05|
|Charlie|Blue Sharks|2025-11-05|
|Charlie|Blue Sharks|2025-11-05|
|David|Blue Sharks|2025-11-05|
|Victor|Blue Sharks|2025-11-05|
|Xander|Blue Sharks|2025-11-05|
|Eve|Green Eagles|2025-11-05|
|Frank|Green Eagles|2025-11-05|
|Grace|Yellow Tigers|2025-11-05|
|Hank|Yellow Tigers|2025-11-05|
|Ivy|Black Panthers|2025-11-05|
|Jack|Black Panthers|2025-11-05|
|Kate|White Wolves|2025-11-05|
|Leo|White Wolves|2025-11-05|
|Mia|Orange Foxes|2025-11-05|
|Ned|Orange Foxes|2025-11-05|
|Olivia|Silver Bulls|2025-11-05|
|Paul|Silver Bulls|2025-11-05|
|Quinn|Golden Hawks|2025-11-05|
|Rachel|Golden Hawks|2025-11-05|
|Sam|Purple Snakes|2025-11-05|
|Tina|Purple Snakes|2025-11-05|

### 3. Annährung
`select p.player_name, t.team_name, m.match_date`
`from matches m, players p, teams t, player_matches pm`
`where pm.match_id = 5` 
`AND pm.player_id = p.player_id`
`AND p.team_id =t.team_id;`

Ich brauche Matches nicht um die id fest zustellen. Sie ist Teil von Player_Matches

|[player_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=p&sql_query=select+p.player_name%2C+t.team_name%2C+m.match_date%0D%0Afrom+matches+m%2C+players+p%2C+teams+t%2C+player_matches+pm%0D%0Awhere+pm.match_id+%3D+5+%0D%0AAND+pm.player_id+%3D+p.player_id%0D%0AAND+p.team_id+%3Dt.team_id++%0AORDER+BY+%60p%60.%60player_name%60+ASC&sql_signature=c26e0d8e7d23681d5f6b80fdf5c16783eb4610f47462114ab3bd9b5a072dd465&session_max_rows=25&is_browse_distinct=0)|[team_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=p&sql_query=select+p.player_name%2C+t.team_name%2C+m.match_date%0D%0Afrom+matches+m%2C+players+p%2C+teams+t%2C+player_matches+pm%0D%0Awhere+pm.match_id+%3D+5+%0D%0AAND+pm.player_id+%3D+p.player_id%0D%0AAND+p.team_id+%3Dt.team_id++%0AORDER+BY+%60t%60.%60team_name%60+ASC&sql_signature=88bda0be9aea6c366bec122aceb8dc96fd56e608791921ccb4c92b63319b9a18&session_max_rows=25&is_browse_distinct=0)|[match_date](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=p&sql_query=select+p.player_name%2C+t.team_name%2C+m.match_date%0D%0Afrom+matches+m%2C+players+p%2C+teams+t%2C+player_matches+pm%0D%0Awhere+pm.match_id+%3D+5+%0D%0AAND+pm.player_id+%3D+p.player_id%0D%0AAND+p.team_id+%3Dt.team_id++%0AORDER+BY+%60m%60.%60match_date%60+DESC&sql_signature=07d66dc2b9e5b177bcb6207dc8fb3cccb118885e76dbe3f8cd18ed590b87331e&session_max_rows=25&is_browse_distinct=0)||
|---|---|---|---|
|Ivy|Black Panthers|2025-11-01|
|Jack|Black Panthers|2025-11-01|
|Ivy|Black Panthers|2025-11-02|
|Jack|Black Panthers|2025-11-02|
|Ivy|Black Panthers|2025-11-03|
|Jack|Black Panthers|2025-11-03|
|Ivy|Black Panthers|2025-11-04|
|Jack|Black Panthers|2025-11-04|
|Ivy|Black Panthers|2025-11-05|
|Jack|Black Panthers|2025-11-05|
|Ivy|Black Panthers|2025-11-06|
|Jack|Black Panthers|2025-11-06|
|Ivy|Black Panthers|2025-11-07|
|Jack|Black Panthers|2025-11-07|
|Ivy|Black Panthers|2025-11-08|
|Jack|Black Panthers|2025-11-08|
|Ivy|Black Panthers|2025-11-09|
|Jack|Black Panthers|2025-11-09|
|Ivy|Black Panthers|2025-11-10|
|Jack|Black Panthers|2025-11-10|
|Ivy|Black Panthers|2025-11-11|
|Jack|Black Panthers|2025-11-11|
|Ivy|Black Panthers|2025-11-12|
|Jack|Black Panthers|2025-11-12|

Was stimmt. Datum, Spieler, Mannschaft.
Was stimmt nicht: Wiederholungen
### Teilschritte
 - #### 1
`   select m.match_date from matches m where m.match_id = 5;   `

2025-11-05
- #### 2
`   select m.match_date, p.player_name from matches m, players p where m.match_id = 5;   `
|[match_date](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=matches&sql_query=select++m.match_date%2C+p.player_name%0D%0Afrom+matches+m%2C+players+p%0D%0Awhere+m.match_id+%3D+5++%0AORDER+BY+%60m%60.%60match_date%60+DESC&sql_signature=991c8c32c821a782396fd12cf5dd456ab8eb384306e789f804e277fe4ebb25f9&session_max_rows=25&is_browse_distinct=0)|[player_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=matches&sql_query=select++m.match_date%2C+p.player_name%0D%0Afrom+matches+m%2C+players+p%0D%0Awhere+m.match_id+%3D+5++%0AORDER+BY+%60p%60.%60player_name%60+ASC&sql_signature=7797e5b410c81a2f607bd057abc5d8412bfdea113a0ccfc486a8a4b03fd23ce6&session_max_rows=25&is_browse_distinct=0)|
|---|---|
|2025-11-05|Alice|
|2025-11-05|Bob|
|2025-11-05|Charlie|
|2025-11-05|David|
|2025-11-05|Eve|
|2025-11-05|Frank|
|2025-11-05|Grace|
|2025-11-05|Hank|
|2025-11-05|Ivy|
|2025-11-05|Jack|
|2025-11-05|Kate|
|2025-11-05|Leo|
|2025-11-05|Mia|
|2025-11-05|Ned|
|2025-11-05|Olivia|
|2025-11-05|Paul|
|2025-11-05|Quinn|
|2025-11-05|Rachel|
|2025-11-05|Sam|
|2025-11-05|Tina|
|2025-11-05|Uma|
|2025-11-05|Victor|
|2025-11-05|Wendy|
|2025-11-05|Xander|

Die Ergebnisse stehen in einer Tabelle haben aber nichts miteinander zu tun. Nur die Spieler von dem einen Spiel sind das Ziel.
##### Was verbindet Match und Spieler?
Tabelle player_matches
Vom groben zum feinen kommen.
### Das Select Sieb
#select #join #SelectSieb
- Tabellen über join Verbinden 
	- `player_matches` enthält Informationen zu `players` und `matches` in Form von `player_id` und `match_id`
		- für beide wird ein `join` erstellt
		- `join players p on pm.player_id = p.player_id
		  `join matches m on pm.match_id = m.match_id
			- Um die Information über das Team auszuwählen, brauchen wir die `players` Tabelle als Verbinder
				- `join teams t on p.team_id = t.team_id
				- Damit sind die Verbindungen geschaffen
					- Weitere Einschränkungen kommen über `where`
					- Das `where` kann über `group by`, `order`weiter eingeschränkt werden

##### Lösung
`select m.match_date, p.player_name, t.team_name
`from player_matches pm
`join players p on pm.player_id = p.player_id
`join matches m on pm.match_id = m.match_id
`join teams t on p.team_id = t.team_id
`where m.match_id = 5;

|[match_date](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=m&sql_query=select+m.match_date%2C+p.player_name%2C+t.team_name%0D%0Afrom+player_matches+pm%0D%0Ajoin+players+p+on+pm.player_id+%3D+p.player_id%0D%0Ajoin+matches+m+on+pm.match_id+%3D+m.match_id%0D%0Ajoin+teams+t+on+p.team_id+%3D+t.team_id%0D%0Awhere+m.match_id+%3D+5++%0AORDER+BY+%60m%60.%60match_date%60+DESC&sql_signature=b26427e8fc45486deef90b549bd412558d972379c11d5007495affd830d59c9e&session_max_rows=25&is_browse_distinct=0)|[player_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=m&sql_query=select+m.match_date%2C+p.player_name%2C+t.team_name%0D%0Afrom+player_matches+pm%0D%0Ajoin+players+p+on+pm.player_id+%3D+p.player_id%0D%0Ajoin+matches+m+on+pm.match_id+%3D+m.match_id%0D%0Ajoin+teams+t+on+p.team_id+%3D+t.team_id%0D%0Awhere+m.match_id+%3D+5++%0AORDER+BY+%60p%60.%60player_name%60+ASC&sql_signature=270b72f596bd71314be6fff31bf633a20ad1c8153bbaf3451e25eae2310a2563&session_max_rows=25&is_browse_distinct=0)|[team_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=m&sql_query=select+m.match_date%2C+p.player_name%2C+t.team_name%0D%0Afrom+player_matches+pm%0D%0Ajoin+players+p+on+pm.player_id+%3D+p.player_id%0D%0Ajoin+matches+m+on+pm.match_id+%3D+m.match_id%0D%0Ajoin+teams+t+on+p.team_id+%3D+t.team_id%0D%0Awhere+m.match_id+%3D+5++%0AORDER+BY+%60t%60.%60team_name%60+ASC&sql_signature=027662c17137cab7159676df9e0bc029e819b51e2af0279b5c69e69ce4bddd66&session_max_rows=25&is_browse_distinct=0)|
|---|---|---|---|
|2025-11-05|Ivy|Black Panthers|
|2025-11-05|Jack|Black Panthers|

## 4. Erstelle ein Query, dass alle Spieler für Team 3 anzeigt. (2 Ergebnisse)

`SELECT p.player_name
`from players p
`where p.team_id = 3;

| [player_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=players&sql_query=SELECT+p.player_name%0D%0Afrom+players+p%0D%0Awhere+p.team_id+%3D+3++%0AORDER+BY+%60p%60.%60player_name%60+ASC&sql_signature=4eef65aa9f6ca72337a0b0b3debb5ae817307414905d60d260c9d8d0e8df6b41&session_max_rows=25&is_browse_distinct=0) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Eve                                                                                                                                                                                                                                                                                                                                      |
| Frank                                                                                                                                                                                                                                                                                                                                    |

## 5. Erstelle ein Query, dass für jedes Team anzeigt, wie viele Spiele gespielt wurden. (12 Ergebnisse)
Jedes Spiel hat zwei Teams `home_team_id` und `away_team_id`
Die Summe der Spiele muss berechnet werden `count`
Welche Tabelle hat die meisten Informationen? 
`matches` 

`select count(m.away_team_id), count(m.home_team_id)
`from matches m;

### Lösung
gezählt werden die Spiele über die `match_id` nicht die Teams bei den Spielen. Das war mein Denkfehler
#### Schritte
`select t.team_name from teams t;`

-------

``select t.team_name
``from teams t
``join matches m on t.team_id = m.away_team_id or t.team_id = m.home_team_id;`

-------
``select t.team_name
``from teams t
``join matches m on t.team_id = m.away_team_id or t.team_id = m.home_team_id
``group by t.team_id;


---
``select t.team_name, count(m.match_id)
``from teams t
``join matches m on t.team_id = m.away_team_id or t.team_id = m.home_team_id
``group by t.team_id;

----------
``select t.team_name, COUNT(m.match_id) as SpielAnzahl
``from teams t
``join matches m on t.team_id = m.away_team_id or t.team_id = m.home_team_id
``group by t.team_id;

|[team_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=teams&sql_query=select+t.team_name%2C+COUNT%28m.match_id%29+as+SpielAnzahl%0D%0Afrom+teams+t%0D%0Ajoin+matches+m+on+t.team_id+%3D+m.away_team_id+or+t.team_id+%3D+m.home_team_id%0D%0Agroup+by+t.team_id++%0AORDER+BY+%60t%60.%60team_name%60+ASC&sql_signature=cd9ce20924ea56daf4e3d4481e00422553fd28d6397cf15c41b962756630df53&session_max_rows=25&is_browse_distinct=0)|[SpielAnzahl](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=teams&sql_query=select+t.team_name%2C+COUNT%28m.match_id%29+as+SpielAnzahl%0D%0Afrom+teams+t%0D%0Ajoin+matches+m+on+t.team_id+%3D+m.away_team_id+or+t.team_id+%3D+m.home_team_id%0D%0Agroup+by+t.team_id++%0AORDER+BY+%60SpielAnzahl%60+ASC&sql_signature=e4d652151ae51f84bfb9153088fd8987321b690d32c503ef2f4c0aa3468b2be6&session_max_rows=25&is_browse_distinct=0)|
|---|---|---|
|Red Lions|3|
|Blue Sharks|3|
|Green Eagles|3|
|Yellow Tigers|3|
|Black Panthers|2|
|White Wolves|2|
|Orange Foxes|2|
|Silver Bulls|2|
|Golden Hawks|2|
|Purple Snakes|2|

----------
##### Bonus
#having
Weitere Einschränkung des Ergebnis im Letzte Schritt 

``select t.team_name, count(m.match_id) as SpielAnzahl
``from teams t
``join matches m on t.team_id = m.away_team_id or t.team_id = m.home_team_id
``group by t.team_id
``HAVING SpielAnzahl >2;

| [team_name](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=teams&sql_query=select+t.team_name%2C+count%28m.match_id%29+as+SpielAnzahl%0D%0Afrom+teams+t%0D%0Ajoin+matches+m+on+t.team_id+%3D+m.away_team_id+or+t.team_id+%3D+m.home_team_id%0D%0Agroup+by+t.team_id%0D%0AHAVING+SpielAnzahl+%3E2++%0AORDER+BY+%60t%60.%60team_name%60+ASC&sql_signature=d9e9745ba0fc7fdf6740894dd2dadb116c7e85bf514b9f2646c48f1360c8c3f6&session_max_rows=25&is_browse_distinct=0) | [SpielAnzahl](http://localhost/phpmyadmin/index.php?route=/sql&db=soccer&table=teams&sql_query=select+t.team_name%2C+count%28m.match_id%29+as+SpielAnzahl%0D%0Afrom+teams+t%0D%0Ajoin+matches+m+on+t.team_id+%3D+m.away_team_id+or+t.team_id+%3D+m.home_team_id%0D%0Agroup+by+t.team_id%0D%0AHAVING+SpielAnzahl+%3E2++%0AORDER+BY+%60SpielAnzahl%60+ASC&sql_signature=813540d0d64673ae080620ac4f3864469018d62426758dc2e1b00408c6df0f58&session_max_rows=25&is_browse_distinct=0) |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| Red Lions                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |
| Blue Sharks                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |
| Green Eagles                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |
| Yellow Tigers                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |

#alias
Alias für Tabellen und Collums sind VariablenNamen, die für das ganze `select` Query gelten.

Die Zahl in Klammern sind die Anzahl Ergebnisse, die ich bei mir lokal herausbekommen habe. Das kann quasi als Checksumme dienen.

