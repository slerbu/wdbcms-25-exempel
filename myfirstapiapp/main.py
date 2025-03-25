import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

PORT=8280

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def hello():
    msg = "Några populärä SOA-implementationer:"
    soa_protocols = ["SOAP", "REST", "GraphQL", "gRPC"]
    mydict = { "message": "skibidi toilet", "myList": soa_protocols }
    return mydict

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        ssl_keyfile="/etc/letsencrypt/privkey.pem",
        ssl_certfile="/etc/letsencrypt/fullchain.pem",
    )
