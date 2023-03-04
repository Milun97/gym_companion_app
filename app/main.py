import uvicorn
from database.data import create_db, wipe_db, create_data





if __name__ == "__main__":
    wipe_db()
    create_db()
    create_data()
    uvicorn.run("api.v1.endpoints.routes:app", port=8000, reload=True)


