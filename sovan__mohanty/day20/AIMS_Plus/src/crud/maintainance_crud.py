from src.config.db_connct import get_conn
from src.exception.custom_exceptions import RecordNotFoundException

def create_log(log):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO maintenance_log
            (asset_id, maintenance_date, description, performed_by, cost, status, last_updated)
            VALUES (%s,%s,%s,%s,%s,%s,NOW())
        """, (
            log.asset_id, log.maintenance_date, log.description,
            log.performed_by, log.cost, log.status
        ))
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close()
        conn.close()

def update_log(log_id, log):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM maintenance_log WHERE log_id=%s", (log_id,))
        if not cur.fetchone():
            raise RecordNotFoundException("Log not found")
        cur.execute("""
            UPDATE maintenance_log SET
            asset_id=%s, maintenance_date=%s, description=%s,
            performed_by=%s, cost=%s, status=%s, last_updated=NOW()
            WHERE log_id=%s
        """, (
            log.asset_id, log.maintenance_date, log.description,
            log.performed_by, log.cost, log.status, log_id
        ))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def delete_log(log_id):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM maintenance_log WHERE log_id=%s", (log_id,))
        conn.commit()
        if cur.rowcount == 0:
            raise RecordNotFoundException("Log not found")
    finally:
        cur.close()
        conn.close()

def list_logs(status=None):
    conn = get_conn()
    cur = conn.cursor()
    try:
        if status:
            cur.execute("SELECT * FROM maintenance_log WHERE status=%s", (status,))
        else:
            cur.execute("SELECT * FROM maintenance_log")
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def get_log(log_id):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM maintenance_log WHERE log_id=%s", (log_id,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()

def update_status(log_id, status):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE maintenance_log SET status=%s, last_updated=NOW() WHERE log_id=%s",
                    (status, log_id))
        conn.commit()
        if cur.rowcount == 0:
            raise RecordNotFoundException("Log not found")
    finally:
        cur.close()
        conn.close()

def search_logs(keyword):
    conn = get_conn()
    cur = conn.cursor()
    try:
        like = f"%{keyword}%"
        cur.execute("""
            SELECT * FROM maintenance_log
            WHERE description LIKE %s OR performed_by LIKE %s
        """, (like, like))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def count_logs():
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) AS total FROM maintenance_log")
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()
