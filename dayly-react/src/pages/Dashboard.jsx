import { useAuth } from '../context/AuthContext';

export default function Dashboard() {
  const { user } = useAuth();

  return (
    <div className="text-center mt-10">
      <h1 className="text-3xl font-bold">Dashboard</h1>
      {user ? (
        <div className="mt-6 space-y-2">
          <p><strong>ID:</strong> {user.id}</p>
          <p><strong>Username:</strong> {user.username}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      ) : (
        <p className="text-gray-600">Loading user info...</p>
      )}
    </div>
  );
}
