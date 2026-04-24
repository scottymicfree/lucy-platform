import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, '..');

const backendDir = path.join(root, 'backend');
const desktopDir = path.join(root, 'desktop');

const env = {
  ...process.env,
  LUCY_ENV: process.env.LUCY_ENV ?? 'dev',
  LUCY_API_HOST: process.env.LUCY_API_HOST ?? '127.0.0.1',
  LUCY_API_PORT: process.env.LUCY_API_PORT ?? '8000'
};

function run(cmd, args, cwd) {
  const p = spawn(cmd, args, { cwd, env, stdio: 'inherit', shell: process.platform === 'win32' });
  p.on('exit', (code) => {
    if (code && code !== 0) process.exit(code);
  });
  return p;
}

// Start backend (assumes venv already created) OR uses system python.
run('python', ['main.py'], backendDir);

// Start Vite dev server (frontend).
run('npm', ['run', 'dev'], path.join(root, 'frontend'));

// Start electron.
run('npx', ['electron', '.'], desktopDir);
