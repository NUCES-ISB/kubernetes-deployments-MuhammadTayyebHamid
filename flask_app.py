from flask import Flask
import psycopg2
import redis

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host="postgres-service",  # PostgreSQL service name in Kubernetes
        database="flaskdb",
        user="flaskuser",
        password="flaskpassword"
    )
    return conn

# Redis connection
redis_host = "redis-service"  # Redis service name in Kubernetes
redis_port = 6379
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    try:
        # PostgreSQL Connection
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()

        # Redis Connection Test
        redis_client.set("message", "Hello from Flask & Redis!")
        message = redis_client.get("message")

        return f"Connected to PostgreSQL: {db_version} <br> Redis says: {message}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
