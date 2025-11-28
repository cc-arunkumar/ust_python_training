from src.config.db_connct import get_conn
from src.exception.custom_exceptions import RecordNotFoundException, DuplicateRecordException

def create_asset(asset):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT asset_id FROM asset_inventory WHERE serial_number=%s", (asset.serial_number,))
        if cur.fetchone():
            raise DuplicateRecordException("serial_number already exists")
        cur.execute("""
            INSERT INTO asset_inventory
            (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date,
             warranty_years, condition_status, assigned_to, location, asset_status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
            asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
            asset.assigned_to, asset.location, asset.asset_status
        ))
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close()
        conn.close()

def update_asset(asset_id, asset):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        if not cur.fetchone():
            raise RecordNotFoundException("Asset not found")
        cur.execute("""
            UPDATE asset_inventory SET
            asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s,
            purchase_date=%s, warranty_years=%s, condition_status=%s, assigned_to=%s,
            location=%s, asset_status=%s
            WHERE asset_id=%s
        """, (
            asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
            asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
            asset.assigned_to, asset.location, asset.asset_status, asset_id
        ))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def delete_asset(asset_id):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        conn.commit()
        if cur.rowcount == 0:
            raise RecordNotFoundException("Asset not found")
    finally:
        cur.close()
        conn.close()

def list_assets(status=None):
    conn = get_conn()
    cur = conn.cursor()
    try:
        if status:
            cur.execute("""
                SELECT DISTINCT serial_number, asset_tag, asset_type, manufacturer, model, purchase_date,
                                warranty_years, condition_status, assigned_to, location, asset_status
                FROM asset_inventory WHERE asset_status=%s
            """, (status,))
        else:
            cur.execute("""
                SELECT DISTINCT serial_number, asset_tag, asset_type, manufacturer, model, purchase_date,
                                warranty_years, condition_status, assigned_to, location, asset_status
                FROM asset_inventory
            """)
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def get_asset(asset_id):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()

def update_status(asset_id, status):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE asset_inventory SET asset_status=%s, WHERE asset_id=%s",
                    (status, asset_id))
        conn.commit()
        if cur.rowcount == 0:
            raise RecordNotFoundException("Asset not found")
    finally:
        cur.close()
        conn.close()

def search_assets(keyword):
    conn = get_conn()
    cur = conn.cursor()
    try:
        like = f"%{keyword}%"
        cur.execute("""
            SELECT * FROM asset_inventory
            WHERE asset_tag LIKE %s OR model LIKE %s OR manufacturer LIKE %s
        """, (like, like, like))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def count_assets():
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) AS total FROM asset_inventory")
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()
