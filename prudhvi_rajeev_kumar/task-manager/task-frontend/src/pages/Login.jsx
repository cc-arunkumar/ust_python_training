import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const AuthPage = () => {
  const [emp_id, setEmpId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [mounted, setMounted] = useState(false);
  const [splitAnimating, setSplitAnimating] = useState(false);
  const [redirectTo, setRedirectTo] = useState("");
  const [errorShake, setErrorShake] = useState(false);
  const [fadeWhite, setFadeWhite] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const t = setTimeout(() => setMounted(true), 60);
    return () => clearTimeout(t);
  }, []);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setErrorShake(false);
    if (!emp_id || !password) {
      setError("Please enter Employee ID and password.");
      toast.error("Please enter Employee ID and password.");
      // small shake for missing fields
      setErrorShake(true);
      setTimeout(() => setErrorShake(false), 600);
      return;
    }

    try {
      setIsLoading(true);
      const resp = await fetch("http://localhost:8000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ emp_id: Number(emp_id), password }),
      });
      const data = await resp.json();
      if (!resp.ok) {
        const msg = data.detail || data.message || data.error || "Invalid credentials";
        throw new Error(msg);
      }

      localStorage.setItem("token", data.access_token || data.token || "");
      localStorage.setItem("emp_id", data.emp_id);
      localStorage.setItem("role", data.role || data.roles || "");

      toast.success("Signed in");
      const role = data.role || data.roles || "";
      // instead of navigating immediately, play split animation then navigate
      let route = "/";
      if (role === "Manager") route = "/manager/dashboard";
      else if (role === "Admin") route = "/admin/employees";
      else if (role === "Employee") route = "/employee/tasks";

      setRedirectTo(route);
      // trigger split animation: left panel slides left, right slides right
      const SPLIT_MS = 1100; // increased split duration
      const FADE_MS = 300; // fade-to-white duration
      setSplitAnimating(true);
      // after split animation, start fade-to-white
      setTimeout(() => setFadeWhite(true), SPLIT_MS);
      // navigate after split + fade complete
      setTimeout(() => {
        navigate(route);
      }, SPLIT_MS + FADE_MS);
    } catch (err) {
      console.error(err);
      setError(err.message || "Login failed");
      toast.error(err.message || "Login failed");
      // trigger a shake animation on error
      setErrorShake(true);
      setTimeout(() => setErrorShake(false), 700);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-400 to-purple-600 p-6">
      <div className="relative w-full max-w-5xl overflow-hidden">
        {/* component-level helper styles for animations (self-contained) */}
        <style>{`
          /* shake for errors */
          @keyframes shakeX { 0%{transform:translateX(0)}25%{transform:translateX(-6px)}50%{transform:translateX(6px)}75%{transform:translateX(-4px)}100%{transform:translateX(0)} }
          .shake { animation: shakeX 0.6s cubic-bezier(.36,.07,.19,.97); }

          /* subtle entrance */
          @keyframes fadeUp { from { transform: translateY(6px); opacity: 0 } to { transform: translateY(0); opacity: 1 } }
          .fade-in-up { animation: fadeUp 640ms cubic-bezier(.22,.9,.3,1) both; }

          /* background float for decorative circles */
          @keyframes floatSlow { 0% { transform: translateY(0) scale(1) } 50% { transform: translateY(-10px) scale(1.02) } 100% { transform: translateY(0) scale(1) } }

          /* JL overlay pulse */
          @keyframes pulseRing { 0% { box-shadow: 0 0 0 0 rgba(79,70,229,0.28) } 70% { box-shadow: 0 0 0 18px rgba(79,70,229,0.02) } 100% { box-shadow: 0 0 0 0 rgba(79,70,229,0) } }

          /* split behaviour */
          .panel-left, .panel-right { transition: transform 1200ms cubic-bezier(.2,.9,.25,1), opacity 900ms ease, filter 900ms ease; transform-origin: center; }
          .panel-left.split { transform: translateX(-120%) rotateY(8deg) scale(0.96); opacity: 0; filter: blur(4px) saturate(.9); }
          .panel-right.split { transform: translateX(120%) rotateY(-8deg) scale(0.96); opacity: 0; filter: blur(4px) saturate(.9); }

          /* overlay fade-to-white */
          .fade-white { transition: opacity 360ms ease; }

          /* animated background circles */
          .bg-circle { animation: floatSlow 6s ease-in-out infinite; }

          /* JL badge ring */
          .jl-ring { animation: pulseRing 1600ms infinite; }
        `}</style>

        {/* optional overlay shown during split animation - enhanced */}
        {splitAnimating && (
          <div className="fixed inset-0 z-40 flex items-center justify-center pointer-events-none">
            <div className="bg-white bg-opacity-0 rounded-full p-6 shadow-xl flex items-center gap-6">
              <div className="relative">
                <div className="w-16 h-16 rounded-full bg-indigo-600 text-white flex items-center justify-center font-bold text-lg jl-ring">JL</div>
                <div className="absolute -inset-3 rounded-full opacity-40" />
              </div>
              <div className="text-gray-800 font-semibold text-xl">Taking you to your workspace...</div>
            </div>
          </div>
        )}

        {/* fade-to-white overlay shown after splitAnimating */}
        <div className={`fixed inset-0 z-50 pointer-events-none bg-white transition-opacity duration-300 ${fadeWhite ? 'opacity-100' : 'opacity-0'}`} />
        {/* decorative background circles */}
        <div className="pointer-events-none absolute -left-24 -top-24 w-80 h-80 rounded-full bg-gradient-to-tr from-indigo-500 to-purple-600 opacity-40 blur-3xl transform scale-110"></div>
        <div className="pointer-events-none absolute -right-24 -bottom-24 w-96 h-96 rounded-full bg-gradient-to-tr from-pink-500 to-yellow-400 opacity-30 blur-3xl transform scale-110"></div>

        <div className={`bg-white rounded-xl shadow-2xl overflow-hidden grid grid-cols-1 md:grid-cols-2 transform-gpu` }>
          {/* left showcase */}
          <div className={`hidden md:flex panel-left items-center justify-center bg-gradient-to-br from-indigo-700 to-purple-800 p-10 ${splitAnimating ? 'split' : ''}`}>
            <div className={`text-white text-center max-w-xs transform transition-all duration-700 ${mounted ? 'opacity-100 translate-y-0 fade-in-up' : 'opacity-0 translate-y-6'}`}>
              <h1 className="text-4xl font-extrabold tracking-tight">Jira Lite</h1>
              <p className="mt-4 text-sm opacity-90">A lightweight task management experience designed for teams.</p>
              <div className="mt-8 bg-white bg-opacity-10 rounded-xl p-4">
                <div className="text-xs uppercase opacity-90">Organize</div>
                <div className="text-sm mt-1">Prioritize tasks, collaborate quickly.</div>
              </div>
            </div>
          </div>

          {/* right form */}
          <div className={`p-8 md:p-12 panel-right flex items-center ${splitAnimating ? 'split' : ''}`}>
            <div className={`w-full max-w-md mx-auto transition-all duration-500 ${mounted ? 'opacity-100 translate-y-0 fade-in-up' : 'opacity-0 -translate-y-4'}`}>
              <div className="mb-6 text-center">
                <div className="inline-flex items-center justify-center w-12 h-12 bg-indigo-600 text-white rounded-full text-xl font-bold">JL</div>
                <h2 className="mt-4 text-2xl font-semibold text-gray-800">Welcome back</h2>
                <p className="text-sm text-gray-500 mt-1">Sign in to continue to Jira Lite</p>
              </div>

              {error && <div className={`mb-4 text-sm text-red-600 text-center ${errorShake ? 'shake' : ''}`}>{error}</div>}

              <form onSubmit={handleLogin} className="space-y-4">
                <div>
                  <label className="text-xs text-gray-600">Employee ID</label>
                  <input
                    type="text"
                    value={emp_id}
                    onChange={(e) => setEmpId(e.target.value)}
                    className={`mt-1 w-full border border-gray-200 rounded-md p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500 ${errorShake ? 'shake' : ''}`}
                    placeholder="Enter your employee ID"
                    required
                  />
                </div>

                <div>
                  <label className="text-xs text-gray-600">Password</label>
                  <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="mt-1 w-full border border-gray-200 rounded-md p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                    placeholder="Enter your password"
                    required
                  />
                </div>

                <div className="flex items-center justify-between">
                  <a className="text-sm text-indigo-600 hover:underline" href="#">Forgot password?</a>
                </div>

                <button type="submit" disabled={isLoading} className="w-full inline-flex items-center justify-center gap-3 bg-indigo-600 hover:bg-indigo-700 text-white py-3 rounded-md font-semibold transition transform active:scale-95">
                  <span className={`inline-flex items-center gap-3 ${isLoading ? 'opacity-100' : 'opacity-100'}`}>
                    {isLoading && (
                      <svg className="w-5 h-5 animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle><path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path></svg>
                    )}
                    <span>{isLoading ? 'Signing in...' : 'Sign in'}</span>
                  </span>
                </button>
              </form>

              <p className="mt-6 text-center text-xs text-gray-400">© {new Date().getFullYear()} Jira Lite • Built with care</p>
            </div>
          </div>
        </div>

        <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick pauseOnFocusLoss draggable pauseOnHover />
      </div>
    </div>
  );
};

export default AuthPage;
