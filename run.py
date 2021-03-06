from imp import reload
import uvicorn

BACK_PORT = 8000
BACK_IP = "192.168.0.9"

def runBack():
    uvicorn.run("main:app", host=BACK_IP, port=BACK_PORT, log_level="info", reload=True)

if __name__ == "__main__":
    runBack()