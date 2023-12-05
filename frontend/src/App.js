import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import PlayerStats from './playerstats';
import TeamStats from './teamstats';
import Extra from './extra'; // Import the Extra component
import './App.css';

function App() {
  return (
    <Router>
      <div>
        <nav>
          {/* Navigation links */}
          <ul>
            <li>
              <Link to="/player-stats">Player Stats</Link>
            </li>
            <li>
              <Link to="/team-stats">Team Stats</Link>
            </li>
            <li>
              <Link to="/extra">Extra</Link> {/* Link to the Extra component */}
            </li>
          </ul>
        </nav>

        {/* Route components */}
        <Routes>
          <Route path="/player-stats" element={<PlayerStats />} />
          <Route path="/team-stats" element={<TeamStats />} />
          <Route path="/extra" element={<Extra />} /> {/* Route for the Extra component */}
          {/* Add more routes as needed */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
