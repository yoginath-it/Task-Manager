import asyncio
import asyncpg
import logging

logger = logging.getLogger("uvicorn")
logging.basicConfig(level=logging.INFO) 

async def get_db_connection():
    try:
        conn = await asyncpg.connect(
            user="yogi", 
            password="password",
            database="taskmanager", 
            host="localhost",    
            port="5432",    
        )
        logger.info("Connected to the database successfully.")
        yield conn
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise
    finally:
        await conn.close()

async def test_connection():
    try:
        async for conn in get_db_connection():
            logger.info("Test query execution.")
            await conn.execute("SELECT 1")
    except Exception as e:
        logger.error(f"Test failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())
