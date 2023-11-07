

-- Query 1 - Full player stats for Luka Donic <3 in the 2018 season
SELECT
    * 
FROM
    player_stats ps
WHERE
    ps.nbapersonid = 1629029 AND
    season = 2018;


-- Query 2 - Full Team stats for the Milwaukee Bucks in the 2017 season
SELECT
    *
FROM
    team_stats ts
WHERE
    ts.nbateamid = 1610612749 AND
    season = 2017;


-- Query 3 - Finds Awards Given to Kawhi Leanard in the 2019 season
SELECT
    CASE
        WHEN `All NBA Defensive First Team` IS NOT NULL THEN 'All NBA Defensive First Team'
        WHEN `All NBA Defensive Second Team` IS NOT NULL THEN 'All NBA Defensive Second Team'
        WHEN `All NBA First Team` IS NOT NULL THEN 'All NBA First Team'
        WHEN `All NBA Second Team` IS NOT NULL THEN 'All NBA Second Team'
        WHEN `All NBA Third Team` IS NOT NULL THEN 'All NBA Third Team'
        WHEN `All Rookie First Team` IS NOT NULL THEN 'All Rookie First Team'
        WHEN `All Rookie Second Team` IS NOT NULL THEN 'All Rookie Second Team'
        WHEN `Bill Russell NBA Finals MVP` IS NOT NULL THEN 'Bill Russell NBA Finals MVP'
        WHEN `Player Of The Month` IS NOT NULL THEN 'Player Of The Month'
        WHEN `Player Of The Week` IS NOT NULL THEN 'Player Of The Week'
        WHEN `Rookie Of The Month` IS NOT NULL THEN 'Rookie Of The Month'
        WHEN `all_star_game` IS NOT NULL THEN 'All Star Game'
        WHEN `rookie_all_star_game` IS NOT NULL THEN 'Rookie All Star Game'
        WHEN `allstar_rk` IS NOT NULL THEN 'All-Star Ranking'
        WHEN `Defensive Player Of The Year_rk` IS NOT NULL THEN 'Defensive Player Of The Year Ranking'
        WHEN `Most Improved Player_rk` IS NOT NULL THEN 'Most Improved Player Ranking'
        WHEN `Most Valuable Player_rk` IS NOT NULL THEN 'Most Valuable Player Ranking'
        WHEN `Rookie Of The Year_rk` IS NOT NULL THEN 'Rookie Of The Year Ranking'
        WHEN `Sixth Man Of The Year_rk` IS NOT NULL THEN 'Sixth Man Of The Year Ranking'
        WHEN `all_nba_points_rk` IS NOT NULL THEN 'All NBA Points Ranking'
        WHEN `all_rookie_points_rk` IS NOT NULL THEN 'All Rookie Points Ranking'
        ELSE 'Unknown Award'
    END AS `Award Name`
FROM 
    awards_data
WHERE
    nbapersonid = 202695 AND
    season = 2019;


-- Query 4 - Finds teams and where they are from
SELECT
    t.city AS City,
    t.nickname AS Team_Names
FROM
    teams t;

-- Query 5 - Finds the total points scored for Luka Doncic in the 2019 season
SELECT
    t.nickname AS 'Team Name',
    p.player_name AS 'Player Name',
    ps.points AS 'Points Scored',
    s.season AS 'Season'
FROM
    teams t,
    players p,
    player_stats ps,
    seasons s
WHERE
    ps.nbapersonid = 1629029 AND
    s.season = 2019 AND
    t.team_id = p.team_id AND
    p.player_id = ps.nbapersonid AND
    ps.season = s.season
LIMIT
    1;


-- Query 6 - Find what two teams played against each other on a certain day
SELECT
    g.game_date_est AS 'Game Date',
    HT.nickname AS 'Home Team',
    VT.nickname AS 'Visiting Team'
FROM
    games g,
    teams VT,
    teams HT
WHERE 
    g.home_team_id = HT.team_id AND
    g.visitor_team_id = VT.team_id
LIMIT
    1;


-- Query 7 - Find the person who scored the lowest amount of points
SELECT
    MIN(ps.points) AS 'Min Points Scored',
    ps.player AS 'Player',
    t.nickname AS 'Team'
FROM
    player_stats ps,
    teams t
WHERE
    ps.nbateamid = t.team_id
GROUP BY
    ps.player,
    t.nickname
LIMIT
    1;

-- Query 8 - 
SELECT
    p.player AS 'Player',
    p.season AS 'Season',
    t.nickname AS 'Team'
FROM
    (SELECT
        ps.player,
        ps.season
     FROM
        player_stats ps
     WHERE
        ps.nbapersonid = 202681
     GROUP BY
        ps.player, ps.season) p
JOIN teams t ON t.team_id = (
    SELECT
        tt.team_id
    FROM
        player_stats pp
    JOIN teams tt ON tt.team_id = pp.nbateamid
    WHERE
        pp.nbapersonid = 202681 AND 
        pp.player = p.player AND
        pp.season = p.season
    LIMIT 1
);


-- Query 9
SELECT
    pt2.Team,
    pt2.Conference,
    pt2.Wins
FROM
    (SELECT
        r.team AS 'Team',
        r.conference AS 'Conference',
        MAX(r.w) AS 'Wins'
    FROM 
        ranking r
    WHERE
        r.standingsdate = '2022-12-22'
    GROUP BY
        r.team, r.conference) AS pt2
ORDER BY pt2.Wins DESC;


-- Query 10
SELECT
    DISTINCT r.team AS Teams,
    r.conference AS Conference
FROM
    ranking r;




-- Query 11: Comparing two teams 

SELECT team, season, games, off_rtg, def_rtg, net_rtg, W, L
FROM team_stats
WHERE team IN ('CHI', 'ATL') AND season = 2017;

-- Query 12:Finding the name and the MVP of the league 

SELECT PLAYER_NAME , nbapersonid
FROM awards_data a 
JOIN players p on p.PLAYER_ID = a.nbapersonid
WHERE a.`Most Valuable Player_rk` = 1
AND a.season = 2017 
and p.SEASON = 2017;

-- Query 13: Season max for mvp in 2017

SELECT 
    p.PLAYER_NAME,
    (SELECT MAX(gd.PTS) 
     FROM games_details gd
     WHERE gd.PLAYER_ID = p.PLAYER_ID
    ) AS MaxPoints
FROM 
    players p
WHERE 
    p.PLAYER_ID IN (SELECT a.nbapersonid
                    FROM awards_data a
                    WHERE a.`Most Valuable Player_rk` = 1
                    AND a.season = 2017)
Limit 1;


-- Query 14: Show all the teams that Journeyman ISh smtih has playerd for 

SELECT DISTINCT 
    p.PLAYER_NAME,
    p.SEASON,
    t.ABBREVIATION,
    t.CITY,
    t.NICKNAME
FROM 
    players p
JOIN 
    teams t ON p.TEAM_ID = t.TEAM_ID
WHERE 
    p.PLAYER_NAME = 'Ish Smith'
ORDER BY 
    p.SEASON;



-- Query 14: Show average PPG in that season 

SELECT 
    p.PLAYER_NAME,
    p.SEASON,
    t.ABBREVIATION,
    t.CITY,
    t.NICKNAME,
    SUM(ps.points) AS TotalPoints,
    SUM(ps.games) AS GamesPlayed,
    CASE 
        WHEN SUM(ps.games) > 0 THEN SUM(ps.points) / SUM(ps.games)
        ELSE 0
    END AS AveragePointsPerGame
FROM 
    players p
JOIN 
    teams t ON p.TEAM_ID = t.TEAM_ID
JOIN 
    player_stats ps ON p.PLAYER_ID = ps.nbapersonid AND p.SEASON = ps.season
WHERE 
    p.PLAYER_NAME = 'Ish Smith'
GROUP BY 
    p.PLAYER_NAME,
    p.SEASON,
    t.ABBREVIATION,
    t.CITY,
    t.NICKNAME
ORDER BY 
    p.SEASON;


-- Query 15: Top 10 scorers for 2018 season

SELECT 
    nbapersonid,
    player,
    season,
    team,
    (points / games) AS avg_points_per_game
FROM 
    player_stats
WHERE 
    season = '2018' AND
    games > 0
ORDER BY 
    avg_points_per_game DESC
LIMIT 10;



-- Query 16: The teams with the most wins for every year we have data for 

SELECT 
    ts.season,
    ts.team,
    m.max_wins
FROM 
    team_stats ts
INNER JOIN (
    SELECT 
        season, 
        MAX(W) AS max_wins
    FROM 
        team_stats
    GROUP BY 
        season
) m ON ts.season = m.season AND ts.W = m.max_wins
ORDER BY 
    ts.season;


-- Query 17: Finding the statics of 1st team all nba players in 2017 

SELECT 
    ps.player AS Player,
    ps.season AS Season,
    ROUND(ps.points / ps.games, 2) AS PPG,  -- Points Per Game
    ROUND(ps.tot_reb / ps.games, 2) AS RPG,  -- Rebounds Per Game
    ROUND(ps.ast / ps.games, 2) AS APG,  -- Assists Per Game
    ROUND(ps.steals / ps.games, 2) AS SPG,  -- Steals Per Game
    ROUND(ps.blocks / ps.games, 2) AS BPG,  -- Blocks Per Game
    ROUND(ps.fgp, 2) AS `FG%`,  -- Field Goal Percentage
    ROUND(ps.PER, 2) AS `PER`  -- Player Efficiency Rating
FROM 
    player_stats ps
JOIN 
    awards_data ad ON ps.nbapersonid = ad.nbapersonid AND ps.season = ad.season
WHERE 
    ad.`All NBA First Team` = 1
    AND ad.season = 2018
ORDER BY 
    PPG DESC;


-- Query 18
SELECT
    DISTINCT p.player_name AS Player,
    ps.draftyear AS Draft_Year
FROM
    players p,
    player_stats ps
WHERE
    p.team_id = 1610612758 AND
    p.player_id = ps.nbapersonid
ORDER BY
    Draft_Year;


-- Query 19
SELECT
    DISTINCT p.player_name AS Player
FROM
    players p,
    player_stats ps
WHERE
    ps.season = 2019 AND
    ps.points > 1000 AND
    p.player_id = ps.nbapersonid;


-- Query 20
SELECT
    t.nickname AS Team,
    ps.season AS Season
FROM
    teams t,
    player_stats ps
WHERE
    ps.nbapersonid = 2544 AND
    ps.nbateamid = t.team_id
ORDER BY
    ps.season;
