// Tiny in-app pub/sub for same-window component communication.
const listeners = new Map();

export function subscribe(eventName, fn) {
  if (!listeners.has(eventName)) listeners.set(eventName, new Set());
  listeners.get(eventName).add(fn);
  return () => listeners.get(eventName).delete(fn);
}

export function publish(eventName, payload) {
  const set = listeners.get(eventName);
  if (!set) return;
  set.forEach((fn) => {
    try {
      fn(payload);
    } catch (e) {
      // ignore subscriber errors
      // eslint-disable-next-line no-console
      console.error(`Event handler for ${eventName} failed:`, e);
    }
  });
}

export default { subscribe, publish };
