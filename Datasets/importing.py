import csv
import pymysql

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "501883@le",
    "database": "project",
}

# Connect to the MySQL database
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

# Create table
create_table_sql = """
CREATE TABLE IF NOT EXISTS player_stats (
    nbapersonid INT,
    player VARCHAR(255),
    draftyear INT,
    draftpick INT,
    season YEAR,
    nbateamid INT,
    team VARCHAR(50),
    games INT,
    games_start INT,
    mins INT,
    fgm INT,
    fga INT,
    fgp FLOAT,
    fgm3 INT,
    fga3 INT,
    fgp3 FLOAT,
    fgm2 INT,
    fga2 INT,
    fgp2 FLOAT,
    efg FLOAT,
    ftm INT,
    fta INT,
    ftp FLOAT,
    off_reb INT,
    def_reb INT,
    tot_reb INT,
    ast INT,
    steals INT,
    blocks INT,
    tov INT,
    tot_fouls INT,
    points INT,
    PER FLOAT,
    FTr FLOAT,
    off_reb_pct FLOAT,
    def_reb_pct FLOAT,
    tot_reb_pct FLOAT,
    ast_pct FLOAT,
    stl_pct FLOAT,
    blk_pct FLOAT,
    tov_pct FLOAT,
    usg FLOAT,
    OWS FLOAT,
    DWS FLOAT,
    WS FLOAT,
    OBPM FLOAT,
    DBPM FLOAT,
    BPM FLOAT,
    VORP FLOAT
);
"""
cursor.execute(create_table_sql)

# Insert data from CSV into the table
with open('player_stats.csv', 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        placeholders = ', '.join(['%s'] * len(headers))
        insert_sql = f"INSERT INTO player_stats VALUES ({placeholders});"
        cursor.execute(insert_sql, tuple(row))

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
