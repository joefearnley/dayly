import { useState } from 'react';
import axios from 'axios';
import { useAuth } from '../context/AuthContext';

export default function Login() {
  const { login } = useAuth();
  const [form, setForm] = useState({ datePublished: '', body: '' });
  const [formError, setFormError] = useState('');

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setFormError('');
    setIsLoading(true);

    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}//`, {
        date_published: form.datePublished,
        body: form.body,
      });

      setIsLoading(false);
      window.location.href = '/entries';
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
              type="date"
              name="date_published"
              value={form.datePublished}
              onChange={handleChange}
              placeholder="Date Published"
              className="input"
              required
            />
          </div>
          <div>
            <textarea
              type="text"
              name="body"
              value={form.body}
              onChange={handleChange}
              placeholder="Body"
              className="input"
              required
            />
          </div>
          <div className="text-error text-left text-sm">{ formError }</div>
          <div>
            <button type="submit" className="btn btn-secondary w-full">
              Add Entry
              {isLoading && (<span className="loading loading-spinner loading-xs"></span>)}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}