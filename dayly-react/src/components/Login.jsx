import { useState } from 'react';
import axios from 'axios';

export default function Login() {
  const [form, setForm] = useState({ username: '', password: '' });
  const [formError, setFormError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setFormError('');
    setIsLoading(true);

    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/token/`, {
        username: form.username,
        password: form.password,
      });

      localStorage.setItem('token', response.data.token);
      setIsLoading(false);
      window.location.href = '/dashboard';
    } catch (err) {
      if (err.response.status === 400) {
        setFormError('Invalid username or password');
      }

      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-sm mx-auto mt-10 p-6 bg-white rounded-2xl shadow-md">
      <h2 className="py-3 font-bold text-xl text-center">Login</h2>
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
              type="password"
              name="password"
              value={form.password}
              onChange={handleChange}
              placeholder="password"
              className="input"
              required
            />
          </div>
          <div className="text-error text-left text-sm">{ formError }</div>
          <div>
            <button type="submit" className="btn btn-secondary w-full">
              Login
              {isLoading && (<span className="loading loading-spinner loading-xs"></span>)}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}