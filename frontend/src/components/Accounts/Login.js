import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Login.css"


function Login({ setToken }) {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/api/account/token/obtain/", {
        username,
        password,
      });
      const { access } = response.data;
      setToken(access);
      navigate("/");
    } catch (error) {
      console.error("Login error:", error);
      setError("Unable to login");
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      {error && <div>{error}</div>}
      <form onSubmit={handleLogin} className="login-form">
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
      <div>
        New user?{" "}
        <button onClick={() => navigate("/register")}>Click to register</button>
      </div>
    </div>
  );
}

export default Login;
