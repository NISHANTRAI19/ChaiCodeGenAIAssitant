from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from connectionManager import ConnectionManager
manager = ConnectionManager()
from chat import customer_support
history = []
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    print("request received")

@app.websocket("/customerSupportBot")
async def websocket_endpoint(websocket: WebSocket):
    print("established connection")
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"data received: {data}")
            if data == "exit":
             await manager.send_personal_message(f"Asha krta hu ki aap course ko enjoy krenge", websocket)
             manager.disconnect(websocket)
            res = customer_support(data,history)
            
            await manager.send_personal_message(f"{res}", websocket)
    except Exception as e:
        print(e)
        manager.disconnect(websocket)
    
    return {"message": "Hello World"}
