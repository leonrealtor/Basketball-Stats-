import React, { useState } from 'react';
import axios from 'axios';

function PlayerStats() {
  const [playerName, setPlayerName] = useState('');
  const [season, setSeason] = useState('');
  const [stats, setStats] = useState(null);
  const [teamHistory, setTeamHistory] = useState(null);
  const [awards, setAwards] = useState(null);
  const [avgPPG, setAvgPPG] = useState(null); 

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const statsResponse = await axios.post('http://127.0.0.1:5000/player-stats', { player_name: playerName, season: season });
      setStats(statsResponse.data);

      const teamHistoryResponse = await axios.post('http://127.0.0.1:5000/player_team_history', { player_name: playerName });
      setTeamHistory(teamHistoryResponse.data);

      const response = await axios.post('http://127.0.0.1:5000/player-awards', { player_name: playerName, season: season });
      setAwards(response.data);

      const ppgResponse = await axios.post('http://127.0.0.1:5000/avg_PPG', { player_name: playerName });
      setAvgPPG(ppgResponse.data);
    } catch (error) {
      console.error("Error fetching data", error);
    }
  };

  const renderStatsTable = () => {
    if (!stats || stats.length === 0) {
      return <p>No stats available for this player and season.</p>;
    }

    // Assuming the first tuple in the array represents the desired stats
    const playerStats = stats[0];

    return (
        <div>
          <h3>Stats for {playerName}, Season {season}</h3>
          <table>
            <tbody>
              {/* Display each stat. Adjust the indices as per your data */}
              <tr><td>Games Played:</td><td>{playerStats[7]}</td></tr>
              <tr><td>Points:</td><td>{playerStats[31]}</td></tr>
              <tr><td>Assists:</td><td>{playerStats[26]}</td></tr>
              <tr><td>Rebounds:</td><td>{playerStats[24]}</td></tr>
              <tr><td>Field Goals Made:</td><td>{playerStats[10]}</td></tr>
              <tr><td>Field Goals Attempted:</td><td>{playerStats[11]}</td></tr>
              <tr><td>Field Goal Percentage:</td><td>{playerStats[12]}</td></tr>
              <tr><td>Three-Point Field Goals Made:</td><td>{playerStats[13]}</td></tr>
              <tr><td>Three-Point Field Goals Attempted:</td><td>{playerStats[14]}</td></tr>
              <tr><td>Three-Point Field Goal Percentage:</td><td>{playerStats[15]}</td></tr>
              <tr><td>Free Throws Made:</td><td>{playerStats[20]}</td></tr>
              <tr><td>Free Throws Attempted:</td><td>{playerStats[21]}</td></tr>
              <tr><td>Free Throw Percentage:</td><td>{playerStats[22]}</td></tr>
              <tr><td>Offensive Rebounds:</td><td>{playerStats[23]}</td></tr>
              <tr><td>Defensive Rebounds:</td><td>{playerStats[24]}</td></tr>
              <tr><td>Total Rebounds:</td><td>{playerStats[25]}</td></tr>
              <tr><td>Steals:</td><td>{playerStats[27]}</td></tr>
              <tr><td>Blocks:</td><td>{playerStats[28]}</td></tr>
              <tr><td>Turnovers:</td><td>{playerStats[29]}</td></tr>
              <tr><td>Total Fouls:</td><td>{playerStats[30]}</td></tr>
              {/* Add more rows for each stat you want to display */}
            </tbody>
          </table>
        </div>
      );
    };


  const renderTeamHistory = () => {
    if (!teamHistory || teamHistory.length === 0) {
      return <p>No team history available for this player.</p>;
    }

    return (
      <div>
        <h3>Team History for {playerName}</h3>
        <ul>
          {teamHistory.map((item, index) => (
            <li key={index}>{item[0]} - Season: {item[1]}</li>  // Adjust based on your actual data structure
          ))}
        </ul>
      </div>
    );
  };

  const awardNames = [
    "All NBA Defensive First Team",
    "All NBA Defensive Second Team",
    "All NBA First Team",
    "All NBA Second Team",
    "All NBA Third Team",
    "All Rookie First Team",
    "All Rookie Second Team",
    "Bill Russell NBA Finals MVP",
    "Player of the Month",
    "Player of the Week",
    "Rookie of the Month",
    "All Star Game",
    "Rookie All Star Game",
    "All Star Rank",
    "Defensive Player of the Year Rank",
    "Most Improved Player Rank",
    "MVP Rank",
    "Rookie of the Year Rank",
    "Sixth Man of the Year",
    "All NBA Points Rank",
    "All Rookie Points Rank"
  ];
  
  const renderAwardsList = () => {
    if (!awards || awards.length === 0) {
      return <p>No awards available for this player and season.</p>;
    }
  
    // Combine all tuples into a single array representing the total awards across all years
    const combinedAwards = awards.reduce((acc, curr) => acc.map((num, idx) => num + curr[idx]), new Array(awards[0].length).fill(0));
  
    // Create a list of award names only for the awards that were received (value > 0)
    const receivedAwards = combinedAwards
      .map((value, index) => value > 0 ? awardNames[index] : null)
      .filter(name => name !== null);
  
    return (
      <div>
        <h3>Awards for {playerName}, Season {season}</h3>
        <ul>
          {receivedAwards.map((awardName, index) => (
            <li key={index}>{awardName}</li>
          ))}
        </ul>
      </div>
    );
  };


  const renderAvgPPG = () => {
    if (!avgPPG || avgPPG.length === 0) {
      return <p>No average PPG data available for this player.</p>;
    }
  
    return (
      <div>
        <h3>Average Points Per Game for {playerName}</h3>
        <table>
          <thead>
            <tr>
              <th>Year</th>
              <th>Team</th>
              <th>City</th>
              <th>Nickname</th>
              <th>Total Points</th>
              <th>Games Played</th>
              <th>Avg PPG</th>
            </tr>
          </thead>
          <tbody>
            {avgPPG.map((item, index) => (
              <tr key={index}>
                <td>{item[1]}</td> {/* Year */}
                <td>{item[2]}</td> {/* Team Abbreviation */}
                <td>{item[3]}</td> {/* City */}
                <td>{item[4]}</td> {/* Nickname */}
                <td>{item[5]}</td> {/* Total Points */}
                <td>{item[6]}</td> {/* Games Played */}
                <td>{parseFloat(item[7]).toFixed(2)}</td> {/* Avg PPG */}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };
  


  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" value={playerName} onChange={(e) => setPlayerName(e.target.value)} placeholder="Player Name" />
        <input type="text" value={season} onChange={(e) => setSeason(e.target.value)} placeholder="Season" />
        <button type="submit">Get Stats and Team History</button>
      </form>
      {renderStatsTable()} 
      {renderAwardsList()} {/* Call renderAwardsList here to display the awards */}
      {renderTeamHistory()}
      {renderAvgPPG()}
    </div>
  );
}

export default PlayerStats;
