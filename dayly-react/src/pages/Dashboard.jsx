import { useState } from 'react';
import { useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import Markdown from 'react-markdown';
import { useAuth } from '../context/AuthContext';

export default function Dashboard() {
  const { token } = useAuth();
  const [latestEntries, setLatestEntrie] = useState([]);
  const [loadingLatestEntries, setLoadingLatestEntries] = useState(false);

  const fetchLatestEntries = async () => {
    setLoadingLatestEntries(true);

    try {   
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/entries/`, {
        headers: {
          Authorization: `Token ${token}`,
        },
      });

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
      <h1 className="text-3xl font-bold mb-6">Latest Entries</h1>
      {loadingLatestEntries ? (
        <div className="my-6">
          <span className="">Loading Latest Entries</span>
          <span className="loading loading-dots loading-md ml-5"></span>
        </div>
        ) : (
          <div>
          {latestEntries.length > 0 ? (
            <div className="overflow-x-auto latest-entries">
              {latestEntries.map((entry) => (
                <div key={entry.id} className="py-4 border-b latest-entry">
                  <div className="mb-4">
                    <Link to={`/entries/${entry.slug}`} className="font-bold">{new Date(entry.date_published).toLocaleDateString()}</Link>
                  </div>
                  <div className="body-wrapper">
                    <Markdown>{entry.body}</Markdown>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <h3 className="my-4 font-medium">No entries found.</h3>
          )}
          </div>
      )}
    </div>
  );
}
