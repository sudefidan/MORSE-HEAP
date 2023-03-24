import asyncio
import websockets
import json

async def main():
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        # After joining server will send client unique id.
        message = json.loads(await websocket.recv()) 
        print(message)
        # Get the client_id from the join message
        if message['type'] == 'join_evt': 
            client_id = message['client_id']
        else:
            # If first message is not the join message exit
            print("Did not receive a correct join message") 
        # Send a ping to the server
        await send_echo(websocket, 'ping', client_id)
        # Wait for the 'ping' response from the server
        response = await send_time(websocket)  
        print("The Server Sent Back:")
        print(response) 


async def send_echo(sender,message):
    print('a')
async def send_time(sender):
    print('a')