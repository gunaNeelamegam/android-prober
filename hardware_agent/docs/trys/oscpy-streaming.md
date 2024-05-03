# Streaming response using OSCPY module

* why you need to stream the response ?

    * Use case is we can able to stream the video or audio using the oscpy socket's

## Client Streaming Example

```py
from oscpy.client import OSCClient
from oscpy.server import OSCThreadServer

from time import sleep
from oscpy.parser import format_message
import asyncio
from asyncio import sleep, run

class OSCClientStreaming(OSCClient):
    def __init__(self, address, port, sock=None, encoding='', encoding_errors='strict'):
        super().__init__(address, port, sock, encoding, encoding_errors)


    async def format_message_(self, address, message):
        for i in message:
            message, _ = format_message(address, [i])
            client.sock.sendto(message, (client.address, client.port))
            await sleep(0.1)

    async def send_streaming_response(self, address, iterable):
        await self.format_message_(address, iterable)

client = OSCClientStreaming(address="0.0.0.0", port = 8000)

async def gena():
    i = 0
    while True:
        yield i
        i += 1
        await sleep(0.3)


def gena1():
    while 1:
        yield from range(10, 20)

tasks = set()

async def mark_async(func, *args, **kwargs):
    func(*args, **kwargs)

async def main():
    task = asyncio.create_task(mark_async(client.send_message, b"/echo", [b"hello world"]))
    tasks.add(task)
    task1 = asyncio.create_task(client.send_streaming_response(b"/", gena1()))
    tasks.add(task1)

    # using the wait statement we can able to wait for the event loops task to complete
    await asyncio.wait(tasks)


# handling the asynchrous pattern to streaming the response
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())

```

# Test Oscpy server

```py
from oscpy.server import OSCThreadServer

server = OSCThreadServer()
server.listen(address="0.0.0.0", port= 5000, default= True)

@server.address(b"/echo")
def echo_response(*args):
    print("ECHO :", args)

@server.address(b"/")
def echo_response(*args):
    print("STREAMING :", args)

# you any async operation here and remove the sleep method
sleep(1000)
server.terminate()
server.stop()
```