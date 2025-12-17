export default function ActivityLog({ logs }) {
  return (
    <div
      style={{
        marginTop: "20px",
        background: "#2c2c3c",
        padding: "12px",
        borderRadius: "6px",
        color: "#f5f5f5"
      }}
    >
      <h3>Activity Log</h3>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {logs.length === 0 && <li>No recent activity</li>}
        {logs.map((log, i) => (
          <li key={i} style={{ marginBottom: "6px" }}>
            {log}
          </li>
        ))}
      </ul>
    </div>
  );
}
