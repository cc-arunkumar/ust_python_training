import pymysql
from fastapi import FastAPI,HTTPException
from practice.models.order_models import Orders
from practice.config.db_connection import get_connection

def create_orders(order:Orders):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        sql="""
        INSERT INTO orders(customer_name,product_id,quantity,status)
        VALUES(%s,%s,%s,%s)
        """
        value=(
            order.customer_name,
            order.product_id,
            order.quantity,
            order.status
        )
        cursor.execute(sql,value)
        conn.commit()
        return {"message": "Order created successfully"}

    except Exception as e:
        raise HTTPException(status_code=500,detail="error in creation of order ")
    finally:
        if conn:
            cursor.close()
            conn.close()
def get_orders_by_id(order_id:int):
    try:
        conn=get_connection()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        sql="SELECT * FROM orders WHERE order_id=%s"
        cursor.execute(sql,(order_id,))
        row= cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404,detail=f"order id {order_id} not found")
        return row
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"error in fetching id {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
def get_all_orders():
    try:
        conn= get_connection()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        sql="SELECT * FROM orders"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching order: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
def update_orders(order_id: int, order: Orders):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        UPDATE orders 
        SET customer_name=%s, product_id=%s, quantity=%s, status=%s 
        WHERE order_id=%s
        """
        values = (
            order.customer_name,
            order.product_id,
            order.quantity,
            order.status,
            order_id
        )
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Order id {order_id} not found")

        return {"message": "Order updated successfully", "order_id": order_id}

    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating order: {str(e)}")

    finally:
        if conn:
            cursor.close()
            conn.close()

        
def delete_orders(order_id:int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM orders WHERE order_id=%s"
        cursor.execute(sql, (order_id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"order id {order_id} not found")
        return {"message": "order deleted successfully", "order_id": order_id}
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting order: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()