import mysql.connector

def create_database_connection():
    return mysql.connector.connect(
        host='localhost',
        database='project',
        user='root',
        password='501883@le'
    )

def get_player_stats_for_season(connection, playername, season):
    cursor = connection.cursor()

    query = """
    SELECT
        *
    FROM
        player_stats ps 
    JOIN players p on p.PLAYER_ID = ps.nbapersonid
    WHERE
        p.PLAYER_NAME = %s AND
        ps.season = %s
    LIMIT 1; 
    """

    cursor.execute(query, (playername, season))
    # column_headers = [i[0] for i in cursor.description]
    #we would also have to return this to be able to handle the return 
    results = cursor.fetchall()
    cursor.close()
    print(results)
    return results


def get_player_awards(connection, nbapersonid, season):
    cursor = connection.cursor()
    query = """
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
        nbapersonid = %s AND
        season = %s;
    """
    cursor.execute(query, (nbapersonid, season))
    
    # Fetching column headers
    # column_headers = [i[0] for i in cursor.description]

    results = cursor.fetchall()
    cursor.close()
    return  results

def get_team_stats_for_season(connection, name, season):
    cursor = connection.cursor()
  
    query = """
        SELECT
            *
        FROM
            team_stats ts
        JOIN teams t on t.TEAM_ID = ts.nbateamid
        WHERE
            NICKNAME = %s AND
            ts.season = %s;
    """

    cursor.execute(query, (name, season))
    # column_headers = [i[0] for i in cursor.description]
    #we would also have to return this to be able to handle the return 
    results = cursor.fetchall()
    cursor.close()
    return results


def get_player_names(connection, partial_name):
    cursor = connection.cursor()
    query = """
    SELECT DISTINCT
        PLAYER_NAME
    FROM
        players
    WHERE
        LOWER(PLAYER_NAME) LIKE LOWER(%s)
    ORDER BY
        PLAYER_NAME;
    """

    # Adding wildcards for partial match
    search_pattern = f"%{partial_name}%"

    cursor.execute(query, (search_pattern,))
    results = cursor.fetchall()
    cursor.close()
    return [result[0] for result in results]  





# connection = create_database_connection()
# stats = get_team_stats_for_season(connection,'Lakers', 2012)

# print(stats)
# for record in stats:
#     print(f"Player ID: {record[0]}, Name: {record[1]}, Season: {record[4]}, Team: {record[6]}, Games Played: {record[7]}, Points: {record[-1]}")
#     # Add more fields as per your tuple structure

        # SELECT
        #     * 
        # FROM
        #     player_stats ps
        # WHERE
        #     player = 'Lebron James' AND
        #     season = 2012;




def get_awards(connection, player_name, season):
    cursor = connection.cursor()
    query = """
            SELECT 
                `All NBA Defensive First Team` AS "All NBA Defensive First Time",
                `All NBA Defensive Second Team` AS "All NBA Defensive Second Team",
                `All NBA First Team` AS "All NBA First Team",
                `All NBA Second Team` AS "All NBA Second Team",
                `All NBA Third Team` AS "All NBA Third Team",
                `All Rookie First Team` AS "All Rookie First Team",
                `All Rookie Second Team` AS "All Rookie Second Team", 
                `Bill Russell NBA Finals MVP` AS "Bill Russell NBA Finals MVP",
                `Player Of The Month` AS "Player of the Month",
                `Player Of The Week` AS "Player of the Week",
                `Rookie Of The Month` AS "Rookie of the Month",
                `all_star_game` AS "All Star Game",
                `rookie_all_star_game` AS "Rookie All Star Game",
                `allstar_rk` AS "All Star Rank",
                `Defensive Player Of The Year_rk` AS "Defensive Player of the Year Rank",
                `Most Improved Player_rk` AS "Most Improved Player Rank",
                `Most Valuable Player_rk` AS "MVP Rank",
                `Rookie Of The Year_rk` AS "Rookie of the Year Rank",
                `Sixth Man Of The Year_rk` AS "Sixth Man of the Year",
                `all_nba_points_rk` AS "All NBA Points Rank",
                `all_rookie_points_rk` AS "All Rookie Points Rank"
            FROM
                awards_data ad,
                players p
            WHERE 
                (`All NBA Defensive First Team` > 0 OR
                `All NBA Defensive Second Team` > 0 OR
                `All NBA First Team` > 0 OR
                `All NBA Second Team` > 0 OR
                `All NBA Third Team` > 0 OR
                `All Rookie First Team` > 0 OR
                `All Rookie Second Team` > 0 OR
                `Bill Russell NBA Finals MVP` > 0 OR
                `Player Of The Month` > 0 OR
                `Player Of The Week` > 0 OR
                `Rookie Of The Month` > 0 OR
                `all_star_game` > 0 OR
                `rookie_all_star_game` > 0 OR
                `allstar_rk` > 0 OR
                `Defensive Player Of The Year_rk` > 0 OR
                `Most Improved Player_rk` > 0 OR
                `Most Valuable Player_rk` > 0 OR
                `Rookie Of The Year_rk` > 0 OR
                `Sixth Man Of The Year_rk` > 0 OR
                `all_nba_points_rk` > 0 OR
                `all_rookie_points_rk` > 0) AND
                p.PLAYER_NAME = %s AND
                ad.season = %s AND
                p.PLAYER_ID = ad.nbapersonid
            ORDER BY
                "Award Name";
    """

    cursor.execute(query, (player_name, season)) 
    results = cursor.fetchall()
    cursor.close()
    return results


# connection = create_database_connection()
# stats = get_awards(connection,'Lebron James', 2012)
# print(stats)



def player_team_history(connection, player_name):

    cursor = connection.cursor()
    query = """
        SELECT
            t.nickname AS Team,
            ps.season AS Season
        FROM
            teams t,
            player_stats ps
        WHERE
            ps.player = %s AND
            ps.nbateamid = t.team_id
        ORDER BY
            ps.season;
    """

    cursor.execute(query, (player_name,))
    results = cursor.fetchall()
    cursor.close()
    return results




# Query 16
def most_wins(connection):
    cursor = connection.cursor()
    query = """
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
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def show_avg_PPG(connection, player_name):

    cursor = connection.cursor()
    query = """
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
            p.PLAYER_NAME = %s
        GROUP BY 
            p.PLAYER_NAME,
            p.SEASON,
            t.ABBREVIATION,
            t.CITY,
            t.NICKNAME
        ORDER BY 
            p.SEASON;
    """

    cursor.execute(query, (player_name,))
    results = cursor.fetchall()
    cursor.close()
    return results
# connection = create_database_connection()
# x = show_avg_PPG(connection, 'Lebron James')
# print(x)


def get_stats_of_1st_team(connection, season):

    cursor = connection.cursor()
    query = """
        SELECT 
            ps.player AS Player,
            ps.season AS Season,
            ROUND(ps.points / ps.games, 2) AS PPG,  -- Points Per Game
            ROUND(ps.tot_reb / ps.games, 2) AS RPG,  -- Rebounds Per Game
            ROUND(ps.ast / ps.games, 2) AS APG,  -- Assists Per Game
            ROUND(ps.steals / ps.games, 2) AS SPG,  -- Steals Per Game
            ROUND(ps.blocks / ps.games, 2) AS BPG,  -- Blocks Per Game
            ROUND(ps.fgp, 2) AS 'FG%',  -- Field Goal Percentage
            ROUND(ps.PER, 2) AS 'PER'  -- Player Efficiency Rating
        FROM 
            player_stats ps
        JOIN 
            awards_data ad ON ps.nbapersonid = ad.nbapersonid AND ps.season = ad.season
        WHERE 
            ad.`All NBA First Team` = 1
            AND ad.season = %s
        ORDER BY 
            PPG DESC;
    """

    cursor.execute(query, (season,))
    results = cursor.fetchall()
    cursor.close()
    return results

def top10_scorers (connection, season):
    cursor = connection.cursor()
    query = """
        SELECT 
            player,
            season,
            team,
            ROUND(points / games) AS avg_points_per_game
        FROM 
            player_stats
        WHERE 
            season = %s AND
            games > 0
        ORDER BY 
            avg_points_per_game DESC
        LIMIT 10;
    """

    cursor.execute(query, (season,))
    results = cursor.fetchall()
    cursor.close()
    return results

def team_rank(connection, season):
    cursor = connection.cursor()
    query = """
        SELECT
            RANK() OVER (ORDER BY wins DESC) AS team_rank,
            teams,
            wins
        FROM
            (SELECT
                DISTINCT t.NICKNAME AS teams,
                W AS wins
            FROM
                rankings r
            JOIN
                teams t ON t.TEAM_ID = r.TEAM_ID
            WHERE
                SEASON_ID = %s AND
                G = 82) AS subquery
        ORDER BY
            wins DESC;
    """
    cursor.execute(query, (season,))
    results = cursor.fetchall()
    cursor.close()
    return  results

connection = create_database_connection()
x = team_rank(connection, 2012)
print(x)

