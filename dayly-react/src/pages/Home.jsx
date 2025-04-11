import { Link } from 'react-router-dom';

export default function Home() {
    return (
      <div className="hero bg-base-200 min-h-screen">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="text-5xl font-bold">Write it down.</h1>
            <h2 className="text-3xl font-bold">to review it later.</h2>
            <p className="py-6">
              Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem
              quasi. In deleniti eaque aut repudiandae et a id nisi.
            </p>
            <Link to="/register" className="btn btn-info">Get Started</Link>
          </div>
        </div>
      </div>
    );
  }