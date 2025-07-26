import os
import snowflake.connector


def get_connection():
    return snowflake.connector.connect(
        user='km_api_test',
        password='P@SSW0rd213!',  # You probably want to fix this — loading from .env is better
        account='fa23837.canada-central.azure',
        role='securityadmin',
        warehouse='COMPUTE_WH'
    )

def get_user_roles(username: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SHOW GRANTS TO USER {username}")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return [f"{row[1]}: {row[2]}" for row in results]

def user_exists_partial(username_partial: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        pattern = f"%{username_partial.upper()}%"
        cursor.execute(f"SHOW USERS LIKE '{pattern}'")
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        # Assuming username is the first column in each row
        return [str(row[0]) for row in results]

    except Exception as e:
        print(f"Error checking users: {e}")
        return []