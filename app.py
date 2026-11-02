from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.get("/inventory")
def inventory():
    return jsonify(
        service = "inventory",
        pod = socket.gethostname(),
        item_id= "item-123",
        quantity=10
    )
    
@app.get("/health")
def health():
    return jsonify(status="alive")

@app.get("/ready")
def ready():
    if os.path.exists("/tmp/not-ready"):
        return jsonify(status="not ready"), 503
    return jsonify(status="ready")

port = int(os.environ.get("PORT", "5000"))
app.run(host="0.0.0.0", port=port)