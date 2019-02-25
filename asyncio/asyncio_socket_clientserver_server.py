"""
server.py - AsyncIO Server using StreamReader and StreamWriter
example in another terminal:
    $ nc localhost 2991
    HELLO
    WORLD
    READY
    one
    ECHO 1: one
    two
    ECHO 2: two
    three
    ECHO 3: three
    four
    ECHO 4: four
    five
    ECHO 5: five
    six
    ECHO 6: six
    seven
    ECHO 7: seven
    eight
    ECHO 8: eight
    nine
    ECHO 9: nine
    ten
    ECHO 10: ten
    bye
    BYE
    $
"""

import asyncio
import logging

log = logging.getLogger(__name__)

clients = {}  # task -> (reader, writer)


def accept_client(client_reader, client_writer):
    task = asyncio.Task(handle_client(client_reader, client_writer))
    clients[task] = (client_reader, client_writer)

    def client_done(task):
        del clients[task]
        client_writer.close()
        log.info("End Connection")

    log.info("New Connection")
    task.add_done_callback(client_done)


@asyncio.coroutine
def handle_client(client_reader, client_writer):
    # send a hello to let the client know they are connected
    client_writer.write("HELLO\n".encode())

    # give client a chance to respond, timeout after 10 seconds
    data = yield from asyncio.wait_for(client_reader.readline(),
                                       timeout=10.0)

    if data is None:
        log.warning("Expected WORLD, received None")
        return

    sdata = data.decode().rstrip()
    log.info("Received %s", sdata)
    if sdata != "WORLD":
        log.warning("Expected WORLD, received '%s'", sdata)
        return

    # now be an echo back server until client sends a bye
    i = 0  # sequence number
    # let client know we are ready
    client_writer.write("READY\n".encode())
    while True:
        i = i + 1
        # wait for input from client
        data = yield from asyncio.wait_for(client_reader.readline(),
                                           timeout=10.0)
        if data is None:
            log.warning("Received no data")
            # exit echo loop and disconnect
            return

        sdata = data.decode().rstrip()
        if sdata.upper() == 'BYE':
            client_writer.write("BYE\n".encode())
            break
        response = ("ECHO %d: %s\n" % (i, sdata))
        client_writer.write(response.encode())


def main():
    loop = asyncio.get_event_loop()
    f = asyncio.start_server(accept_client, host=None, port=2991)
    loop.run_until_complete(f)
    loop.run_forever()

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