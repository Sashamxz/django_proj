import { useState } from "react";
import axios from "axios";
import "./Register.css"



function Register() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    // Remove confirmPassword field from formData
    const { confirmPassword, ...data } = formData;

    axios.post("/api/user/create/", data).then((response) => {
      console.log(response.data);
    });
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username:
        <input type="text" name="username" onChange={handleChange} />
      </label>
      <label>
        Email:
        <input type="email" name="email" onChange={handleChange} />
      </label>
      <label>
        Password:
        <input type="password" name="password" onChange={handleChange} />
      </label>
      <label>
        Confirm Password:
        <input
          type="password"
          name="confirmPassword"
          onChange={handleChange}
        />
      </label>
      <button type="submit">Register</button>
    </form>
  );
}

export default Register;
