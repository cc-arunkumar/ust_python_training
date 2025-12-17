export default function Avatar({ name }) {
  const initials = name
    ? name.split(" ").map((n) => n[0]).join("").toUpperCase()
    : "?";

  return (
    <div
      style={{
        background: "#007acc",
        color: "white",
        borderRadius: "50%",
        width: "32px",
        height: "32px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontSize: "14px",
        marginTop: "8px"
      }}
    >
      {initials}
    </div>
  );
}
