from flask import Flask, jsonify, request
from flask_cors import CORS
from connection import *

app = Flask(__name__)

CORS(app)



@app.route('/')
def home():
    return "Welcome to the NBA Stats API!"

@app.route('/player-stats', methods=['POST'])
def post_player_stats():
    data = request.get_json()
    player_name = data['player_name']
    season = data['season']
    connection = create_database_connection()

    print(player_name)
    print(season)
    try:
        stats = get_player_stats_for_season(connection, player_name, season)
    finally:
        connection.close()
    return jsonify(stats)

# @app.route('/player-awards', methods=['POST'])
# def post_player_awards():
#     data = request.get_json()
#     nbaperson = data['player_id']
#     season = data['season']
#     connection = create_database_connection()

#     # nbapersonid = get_player_id_by_name(connection, nbaperson)

#     try:
#         awards = get_player_awards(connection, nbaperson, season)
#     finally:
#         connection.close()
#     return jsonify(awards)


@app.route('/team-stats', methods=['POST'])
def post_team_stats():
    data = request.get_json()
    team_name = data['team_name']
    season = data['seasons']
    print(team_name)
    print(season)
    connection = create_database_connection()
    try:
        teamstats = get_team_stats_for_season(connection, team_name, season,)
    finally:
        connection.close()
    return jsonify(teamstats)



@app.route('/search-players', methods=['GET'])
def search_players():
    partial_name = request.args.get('query', '')  # Get the query parameter from the URL
    connection = create_database_connection()  # Function to connect to your database
    try:
        player_names = get_player_names(connection, partial_name)
    finally:
        connection.close()
    return jsonify(player_names)

@app.route('/player-awards', methods=['POST'])
def post_player_awards():
    data = request.get_json()
    player_name = data.get('player_name')
    season = data.get('season')

    if not player_name or not season:
        return jsonify({"error": "Missing player_name or season"}), 400

    connection = create_database_connection()
    try:
        awards = get_awards(connection, player_name, season)
    finally:
        connection.close()

    return jsonify(awards)

@app.route('/player_team_history', methods=['POST'])
def post_team_history():
    data = request.get_json()
    player_name = data['player_name']
    connection = create_database_connection()
    try:
        player_history = player_team_history(connection, player_name,)
    finally:
        connection.close()
    return jsonify(player_history)


@app.route('/most_wins', methods=['POST'])
def post_most_wins():
    connection = create_database_connection()
    try:
        wins = most_wins(connection)
    finally:
        connection.close()
    return jsonify(wins)


@app.route('/avg_PPG', methods=['POST'])
def post_avg_PPG():
    data = request.get_json()
    player_name = data['player_name']
    connection = create_database_connection()
    try:
        PPG_avg = show_avg_PPG(connection, player_name,)
    finally:
        connection.close()
    return jsonify(PPG_avg)

@app.route('/first_team_stats', methods=['POST'])
def post_first_team_stats():
    data = request.get_json()
    season = data['season']
    connection = create_database_connection()
    try:
        first_team_stats = get_stats_of_1st_team(connection, season,)
    finally:
        connection.close()
    return jsonify(first_team_stats)


@app.route('/top-10-scorers', methods=['POST'])
def post_top10_scorers():
    data = request.get_json()
    season = data['season']
    connection = create_database_connection()
    try:
        top10 = top10_scorers(connection, season,)
    finally:
        connection.close()
    return jsonify(top10)


@app.route('/team_rank', methods=['POST'])
def post_team_rank():
    data = request.get_json()
    season = data['season']
    connection = create_database_connection()
    print(season)
    try:
        team_rank_results = team_rank(connection, season,)
        # print(team_rank_results)
    finally:
        connection.close()
    return jsonify(team_rank_results)

if __name__ == '__main__':
    app.run(debug=True)


