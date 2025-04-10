import { createContext, useContext, useEffect, useState } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(() => localStorage.getItem('token'));
  const [isAuthenticated, setIsAuthenticated] = useState(!!token);
  const [user, setUser] = useState(null);

  useEffect(() => {
    setIsAuthenticated(!!token);
    if (token) {
      fetchUserProfile(token);
    }
  }, [token]);

  const login = (jwt) => {
    localStorage.setItem('token', jwt);
    setToken(jwt);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
  };

  const fetchUserProfile = async (jwt) => {
    try {
      const res = await axios.get('http://localhost:8000/api/profile/', {
        headers: {
          Authorization: `Bearer ${jwt}`,
        },
      });
      setUser(res.data);
    } catch (err) {
      console.error('Failed to fetch user profile:', err);
    }
  };

  return (
    <AuthContext.Provider value={{ token, isAuthenticated, login, logout, user }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
