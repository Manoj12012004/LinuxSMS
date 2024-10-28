import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [token, setToken] = useState(null);
  const [countryOperators, setCountryOperators] = useState([]);

  useEffect(() => {
    if (token) {
      fetchCountryOperators();
    }
  }, [token]);

  const login = async () => {
    const response = await axios.post("http://localhost:8000/login", {
      username: "admin",
      password: "password",
    });
    setToken(response.data.access_token);
  };

  const fetchCountryOperators = async () => {
    const response = await axios.get("http://localhost:8000/country-operator", {
      headers: { Authorization: `Bearer ${token}` },
    });
    setCountryOperators(response.data);
  };

  return (
    <div>
      {!token ? (
        <button onClick={login}>Login</button>
      ) : (
        <div>
          <h1>Dashboard</h1>
          <ul>
            {countryOperators.map((item, index) => (
              <li key={index}>
                {item.country} - {item.operator} - Priority:{" "}
                {item.is_high_priority ? "High" : "Low"}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
