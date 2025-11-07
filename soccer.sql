-- Create teams table
CREATE TABLE teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(50) NOT NULL
);

-- Create players table
CREATE TABLE players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(50) NOT NULL,
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- Create matches table
CREATE TABLE matches (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    match_date DATE NOT NULL,
    home_team_id INT,
    away_team_id INT,
    FOREIGN KEY (home_team_id) REFERENCES teams(team_id),
    FOREIGN KEY (away_team_id) REFERENCES teams(team_id)
);

-- Create player_matches table to represent players who played in matches (many-to-many)
CREATE TABLE player_matches (
    player_id INT,
    match_id INT,
    PRIMARY KEY (player_id, match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);

-- Insert teams
INSERT INTO teams (team_name) VALUES
('Red Lions'),
('Blue Sharks'),
('Green Eagles'),
('Yellow Tigers'),
('Black Panthers'),
('White Wolves'),
('Orange Foxes'),
('Silver Bulls'),
('Golden Hawks'),
('Purple Snakes'),
('Pink Dolphins'),
('Brown Bears');

-- Insert players
INSERT INTO players (player_name, team_id) VALUES
('Alice', 1),
('Bob', 1),
('Charlie', 2),
('David', 2),
('Eve', 3),
('Frank', 3),
('Grace', 4),
('Hank', 4),
('Ivy', 5),
('Jack', 5),
('Kate', 6),
('Leo', 6),
('Mia', 7),
('Ned', 7),
('Olivia', 8),
('Paul', 8),
('Quinn', 9),
('Rachel', 9),
('Sam', 10),
('Tina', 10),
('Uma', 1),
('Victor', 2),
('Wendy', 1),
('Xander', 2);

-- Insert matches
INSERT INTO matches (match_date, home_team_id, away_team_id) VALUES
('2025-11-01', 1, 2),
('2025-11-02', 2, 1),
('2025-11-03', 3, 4),
('2025-11-04', 4, 3),
('2025-11-05', 5, 6),
('2025-11-06', 6, 5),
('2025-11-07', 7, 8),
('2025-11-08', 8, 7),
('2025-11-09', 9, 10),
('2025-11-10', 10, 9),
('2025-11-11', 1, 3),
('2025-11-12', 2, 4);

-- Insert which players played in which matches
INSERT INTO player_matches (player_id, match_id) VALUES
(1, 1),
(2, 1),
(3, 1),
(3, 2),
(4, 2),
(5, 3),
(6, 3),
(7, 4),
(8, 4),
(9, 5),
(10, 5),
(11, 6),
(12, 6),
(13, 7),
(14, 7),
(15, 8),
(16, 8),
(17, 9),
(18, 9),
(19, 10),
(20, 10),
(21, 11),
(22, 12),
(23, 11),
(24, 12);