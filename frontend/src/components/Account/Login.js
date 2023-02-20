import React, { useState } from "react";
import axios from "axios";

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
 

  const handleSubmit = e => {
    e.preventDefault();

    axios.post("/api/accounnt/token", { username, password })
      .then(response => {
        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);
        onLogin();
        history.push("/");
      })
      .catch(error => {
        setError("Invalid username or password.");
      });
  };

  return (
    <div className="login-form">
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      {error && <div>{error}</div>}
      <div>
        <label>Username:</label>
        <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
      </div>
      <button type="submit">Login</button>
    </form>
    </div>
  );
};

export default Login;
