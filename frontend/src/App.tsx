import { useEffect, useState } from 'react';

type Health = { ok: boolean };

export default function App() {
  const [health, setHealth] = useState<Health | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const run = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/health');
        const json = (await res.json()) as Health;
        setHealth(json);
      } catch (e: any) {
        setError(String(e));
      }
    };

    run();
    const t = window.setInterval(run, 2000);
    return () => window.clearInterval(t);
  }, []);

  return (
    <div style={{ fontFamily: 'system-ui', padding: 24, background: '#020617', color: '#e2e8f0', minHeight: '100vh' }}>
      <h1 style={{ margin: 0, fontSize: 24 }}>Lucy Desktop (Electron)</h1>
      <p style={{ opacity: 0.8 }}>Backend health: {health ? String(health.ok) : '…'}</p>
      {error && <pre style={{ whiteSpace: 'pre-wrap', color: '#fca5a5' }}>{error}</pre>}
      <p style={{ opacity: 0.7, marginTop: 16 }}>
        Next: add NodeMesh live view + TwinEarth dashboard, and switch the desktop to load Vite dev server in dev and bundled build in prod.
      </p>
    </div>
  );
}
