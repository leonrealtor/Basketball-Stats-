import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Extra() {
    const [mostWins, setMostWins] = useState([]);
    const [firstTeamStats, setFirstTeamStats] = useState([]);
    const [top10Scorers, setTop10Scorers] = useState([]);
    const [season, setSeason] = useState('');
    const [scorersSeason, setScorersSeason] = useState('');
    const [teamRank, setTeamRank] = useState([]);
    const [rankSeason, setRankSeason] = useState([]);
  

  useEffect(() => {
    // Fetch Teams with Most Wins
    const fetchMostWins = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:5000/most_wins');
        setMostWins(response.data);
      } catch (error) {
        console.error("Error fetching most wins data", error);
      }
    };

    fetchMostWins();
  }, []);

  // Function to fetch First Team Stats
  const fetchFirstTeamStats = async () => {
    if (season) {
      try {
        const response = await axios.post('http://127.0.0.1:5000/first_team_stats', { season: season });
        setFirstTeamStats(response.data);
      } catch (error) {
        console.error("Error fetching first team stats", error);
      }
    }
  };

  const fetchTop10Scorers = async () => {
    if (scorersSeason) {
      try {
        const response = await axios.post('http://127.0.0.1:5000/top-10-scorers', { season: scorersSeason });
        setTop10Scorers(response.data);
      } catch (error) {
        console.error("Error fetching top 10 scorers", error);
      }
    }
  };

  const fetchTeamRank = async () => {
    if (rankSeason) {
      try {
        const response = await axios.post('http://127.0.0.1:5000/team_rank', { season: rankSeason });
        setTeamRank(response.data);
      } catch (error) {
        console.error("Error fetching team rank", error);
      }
    }
  };


  return (
    <div>
      <h3>Teams with Most Wins by Season</h3>
      <ul>
        {mostWins.map((win, index) => (
          <li key={index}>Season {win[0]}: {win[1]} - Wins: {win[2]}</li>
        ))}
      </ul>

      <h3>First Team Stats for Season</h3>
      <input 
        type="text" 
        value={season} 
        onChange={(e) => setSeason(e.target.value)} 
        placeholder="Enter Season" 
      />
      <button onClick={fetchFirstTeamStats}>Fetch First Team Stats</button>
      <ul>
        {firstTeamStats.map((player, index) => (
          <li key={index}>
            {player[0]} ({player[1]}) - PPG: {parseFloat(player[2]).toFixed(2)}, RPG: {parseFloat(player[3]).toFixed(2)}, 
            APG: {parseFloat(player[4]).toFixed(2)}, SPG: {parseFloat(player[5]).toFixed(2)}, BPG: {parseFloat(player[6]).toFixed(2)},
            FG%: {parseFloat(player[7]).toFixed(2)}, PER: {parseFloat(player[8]).toFixed(2)}
          </li>
        ))}
      </ul>
      <h3>Top 10 Scorers for Season</h3>
      <input 
        type="text" 
        value={scorersSeason} 
        onChange={(e) => setScorersSeason(e.target.value)} 
        placeholder="Enter Season for Top 10 Scorers" 
      />
      <button onClick={fetchTop10Scorers}>Fetch Top 10 Scorers</button>
      <ul>
        {top10Scorers.map((scorer, index) => (
          <li key={index}>
            {scorer[0]} ({scorer[1]}, {scorer[2]}) - PPG: {parseFloat(scorer[3]).toFixed(2)}
          </li>
        ))}
      </ul>

      <h3>Team Ranks for Season</h3>
      <input 
        type="text" 
        value={rankSeason} 
        onChange={(e) => setRankSeason(e.target.value)} 
        placeholder="Enter Season for Team Rank" 
      />
      <button onClick={fetchTeamRank}>Fetch Team Ranks</button>
      <table>
        <thead>
          <tr>
            <th>Rank</th>
            <th>Team</th>
            <th>Wins</th>
          </tr>
        </thead>
        <tbody>
          {teamRank.map((team, index) => (
            <tr key={index}>
              <td>{team[0]}</td> {/* Rank */}
              <td>{team[1]}</td> {/* Team */}
              <td>{team[2]}</td> {/* Wins */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Extra;
