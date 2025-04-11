import { useState } from 'react';
import { useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

export default function Dashboard() {
  const [token, setToken] = useState(() => localStorage.getItem('token'));
  const [latestEntries, setLatestEntrie] = useState([]);
  const [loadingLatestEntries, setLoadingLatestEntries] = useState(false);

  const fetchLatestEntries = async () => {
    setLoadingLatestEntries(true);

    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/entries/`, {
        headers: {
          Authorization: `Token ${token}`,
        },
      });

      console.log(`response:`)
      console.log(response)

      setLatestEntrie(response.data);

      setLoadingLatestEntries(false);
    } catch (err) {
      console.log(err);
      setLoadingLatestEntries(false);
    }
  };

  useEffect(() => {
    fetchLatestEntries();
  }, []);

  return (
    <div className="m-10">
      <h1 className="text-3xl font-bold">Latest Entries</h1>
      {loadingLatestEntries ? (
        <div className="my-6">
          <span className="">Loading Latest Entries</span>
          <span className="loading loading-dots loading-md ml-5"></span>
        </div>
        ) : (
          <div>
          {latestEntries.length > 0 ? (
            <div className="overflow-x-auto">
              {latestEntries.map((entry) => (
                <div key={entry.id} className="overflow-x-auto">
                  <div>
                    <Link to="{entry.slug}">{new Date(entry.created_at).toLocaleDateString()}</Link>
                    <div>{entry.title}</div>
                  </div>
                  <div>{entry.content}</div>
                </div>
              ))}
            </div>
          ) : (
            <p>No entries found.</p>
          )}
          </div>
      )}
    </div>
  );
}
