// Normalized remark id generator used across components.
// Creates a deterministic id from a remark object by combining
// role/from, timestamp, author id and a short text snippet.
export function computeRemarkId(r) {
  const from = String(r.from || r.role || "unknown").replace(/\s+/g, "_");
  const ts = String(r.created_at || r.ts || "").replace(/\s+/g, "_");
  const by = String(r.reviewed_by_emp_id || r.byEmpId || r.by || "").replace(
    /\s+/g,
    "_"
  );
  const txt = String(r.review || r.text || r.message || "")
    .slice(0, 30)
    .replace(/\s+/g, "_");
  return `${from}_${ts}_${by}_${txt}`;
}

export default computeRemarkId;
