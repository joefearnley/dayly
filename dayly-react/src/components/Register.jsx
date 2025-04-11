import { useState } from 'react';
import axios from 'axios';

export default function Register() {
  const [form, setForm] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [formError, setFormError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setFormError('');
    setIsLoading(true);

    if (form.password !== form.confirmPassword) {
      setFormError("Passwords don't match");
      return;
    }

    try {
      await axios.post('http://localhost:8000/api/register/', {
        username: form.email,
        email: form.email,
        password: form.password,
      });
      setIsLoading(false);

      alert('Registered successfully! You can now log in.');
    } catch (err) {
      console.error(err);

      if (err.response.status === 400) {
        setFormError(err.response.data.non_field_errors[0]);
      }

      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-sm mx-auto mt-10 p-6 bg-white rounded-2xl shadow-md">
      <h2 className="py-3 font-bold text-xl text-center">Register</h2>
      <div className="space-y-4">
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <input
              type="text"
              name="username"
              value={form.username}
              onChange={handleChange}
              placeholder="@username"
              className="input"
              required
            />
          </div>
          <div>
            <input
              type="email"
              name="email"
              value={form.email}
              onChange={handleChange}
              placeholder="Email"
              className="input"
              required
            />
          </div>
          <div>
            <input
              type="password"
              name="password"
              value={form.password}
              onChange={handleChange}
              placeholder="Password"
              className="input"
              required
            />
          </div>
          <div>
            <input
              type="password"
              name="confirmPassword"
              value={form.confirmPassword}
              onChange={handleChange}
              placeholder="Confirm Password"
              className="input"
              required
            />
          </div>
          <div className="text-error text-left text-sm">{ formError }</div>
          <div>
            <button type="submit" className="btn btn-secondary w-full">
              Register
              {isLoading && (<span className="loading loading-spinner loading-xs"></span>)}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
