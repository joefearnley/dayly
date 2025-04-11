import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Navbar() {
  const { user } = useAuth();

  return (
    <div className="navbar bg-base-100 shadow-sm">
      <div className="flex-1">
        <a href="/" className="btn btn-ghost text-xl">Dayly</a>
      </div>
      <div className="flex-none">
        {user ? (
          <ul className="menu menu-horizontal px-1">
            <li><Link to="/dashboard">Dashboard</Link></li>
            <li>
              <details>
                <summary>Account</summary>
                <ul className="bg-base-100 rounded-t-none p-2">
                  <li><Link to="/account/settings">Settings</Link></li>
                  <li><Link to="/logout">Logout</Link></li>
                </ul>
              </details>
            </li>
          </ul>
        ) : (
          <ul className="menu menu-horizontal px-1">
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/register">Register</Link></li>
          </ul>
        )}
      </div>
    </div>
  );
}