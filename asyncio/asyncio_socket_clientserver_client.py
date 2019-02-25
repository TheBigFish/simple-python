"""
client.py - AsyncIO Server using StreamReader and StreamWriter
This will create 200 client connections to a server running server.py
It will handshake and run similar to this:
Server: HELLO
Client: WORLD
Server: READY
Client: one
Server: ECHO 1: one
...
Client: six
Server: ECHO 6: six
Client: BYE
Server: BYE
"""

import asyncio
import logging

log = logging.getLogger(__name__)

clients = {}  # task -> (reader, writer)


def make_connection(host, port):

    task = asyncio.Task(handle_client(host, port))

    clients[task] = (host, port)

    def client_done(task):
        del clients[task]
        log.info("Client Task Finished")
        if len(clients) == 0:
            log.info("clients is empty, stopping loop.")
            loop = asyncio.get_event_loop()
            loop.stop()

    log.info("New Client Task")
    task.add_done_callback(client_done)


@asyncio.coroutine
def handle_client(host, port):
    log.info("Connecting to %s %d", host, port)
    client_reader, client_writer = yield from asyncio.open_connection(host,
                                                                      port)
    log.info("Connected to %s %d", host, port)
    try:
        # looking for a hello
        # give client a chance to respond, timeout after 10 seconds
        data = yield from asyncio.wait_for(client_reader.readline(),
                                           timeout=10.0)

        if data is None:
            log.warning("Expected HELLO, received None")
            return

        sdata = data.decode().rstrip().upper()
        log.info("Received %s", sdata)
        if sdata != "HELLO":
            log.warning("Expected HELLO, received '%s'", sdata)
            return

        # send back a WORLD
        client_writer.write("WORLD\n".encode())

        # wait for a READY
        data = yield from asyncio.wait_for(client_reader.readline(),
                                           timeout=10.0)

        if data is None:
            log.warning("Expected READY, received None")
            return

        sdata = data.decode().rstrip().upper()
        if sdata != "READY":
            log.warning("Expected READY, received '%s'", sdata)
            return

        echostrings = ['one', 'two', 'three', 'four', 'five', 'six']

        for echostring in echostrings:
            # send each string and get a reply, it should be an echo back
            client_writer.write(("%s\n" % echostring).encode())
            data = yield from asyncio.wait_for(client_reader.readline(),
                                               timeout=10.0)
            if data is None:
                log.warning("Echo received None")
                return

            sdata = data.decode().rstrip()
            log.info(sdata)

        # send BYE to disconnect gracefully
        client_writer.write("BYE\n".encode())

        # receive BYE confirmation
        data = yield from asyncio.wait_for(client_reader.readline(),
                                           timeout=10.0)

        sdata = data.decode().rstrip().upper()
        log.info("Received '%s'" % sdata)
    finally:
        log.info("Disconnecting from %s %d", host, port)
        client_writer.close()
        log.info("Disconnected from %s %d", host, port)


def main():
    log.info("MAIN begin")
    loop = asyncio.get_event_loop()
    for x in range(200):
        make_connection('localhost', 2991)
    loop.run_forever()
    log.info("MAIN end")

if __name__ == '__main__':
    log = logging.getLogger("")
    formatter = logging.Formatter("%(asctime)s %(levelname)s " +
                                  "[%(module)s:%(lineno)d] %(message)s")
    # setup console logging
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(formatter)
    log.addHandler(ch)
    main()