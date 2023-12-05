import React, { useState } from 'react';
import axios from 'axios';

function TeamStats() {
  const [teamName, setTeamName] = useState('');
  const [season, setSeason] = useState('');
  const [teamStats, setTeamStats] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/team-stats', { team_name: teamName, seasons: season });
      setTeamStats(response.data);
    } catch (error) {
      console.error("Error fetching team stats", error);
    }
  };

  const renderTeamStats = () => {
    if (!teamStats || teamStats.length === 0) {
      return <p>No stats available for this team and season.</p>;
    }
    const teamStat = teamStats[0];

    return (
      <div>
        <h3>Stats for {teamName}, Season {season}</h3>
        <table>
          <tbody>
            {/* Display each stat. Adjust the indices as per your data */}
            <tr><td>Team ID:</td><td>{teamStat[0]}</td></tr>
            <tr><td>Team Abbreviation:</td><td>{teamStat[1]}</td></tr>
            <tr><td>Games Played:</td><td>{teamStat[3]}</td></tr>
            <tr><td>Average Points Scored:</td><td>{teamStat[4]}</td></tr>
            <tr><td>Average Points Allowed:</td><td>{teamStat[5]}</td></tr>
            <tr><td>Point Differential:</td><td>{teamStat[6]}</td></tr>
            <tr><td>Wins:</td><td>{teamStat[7]}</td></tr>
            <tr><td>Losses:</td><td>{teamStat[8]}</td></tr>
            {/* Add more rows for each stat you want to display */}
          </tbody>
        </table>
      </div>
    );
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" value={teamName} onChange={(e) => setTeamName(e.target.value)} placeholder="Team Name" />
        <input type="text" value={season} onChange={(e) => setSeason(e.target.value)} placeholder="Season" />
        <button type="submit">Get Team Stats</button>
      </form>
      {renderTeamStats()}
    </div>
  );
}

export default TeamStats;
