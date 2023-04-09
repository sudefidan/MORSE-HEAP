import asyncio
import websockets
import json
from heap import *


async def main():
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        # After joining server will send client unique id.
        message = json.loads(await websocket.recv()) 
        print(message)

async def send_message(websocket, message, client_id): 
    outward_message = {
        'type' : 'morse_evt',
        'client_id': client_id,
        'payload': message
    }

    await websocket.send(json.dumps(outward_message))

async def recv_message(websocket):
    message = json.loads(await websocket.recv()) 
    return message['payload']

async def send_echo(sender, msg):
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        # After joining server will send client unique id.
        message = json.loads(await websocket.recv())
        # Get the client_id from the join message
        if message['type'] == 'join_evt': 
            client_id = message['client_id']

        #ham encode 
        #ECHO DE S =MSG=(
        morse = MorseHeap()
        encoded = morse.encode_ham(sender, 'echo', msg)
        # Send a ping to the server
        await send_message(websocket, encoded, client_id)
        # Wait for the 'ping' response from the server
        response = await recv_message(websocket)
        return morse.decode_bt(response)

async def send_time(sender):
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        # After joining server will send client unique id.
        message = json.loads(await websocket.recv())
        # Get the client_id from the join message
        if message['type'] == 'join_evt': 
            client_id = message['client_id']
        #ham encode
        morse = MorseHeap()
        encoded = morse.encode_ham(sender, 'time', 'msg')
        # Send a ping to the server
        await send_message(websocket,encoded , client_id)
        # Wait for the 'ping' response from the server
        response = await recv_message(websocket)
        return morse.decode_bt(response)

