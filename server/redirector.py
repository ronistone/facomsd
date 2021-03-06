from asyncService import AsyncService
from queue import Empty
from grpc import StatusCode

class Redirector(AsyncService):


    def __init__(self, node, toRedirect, threadName,):
        AsyncService.__init__(self)
        self.setName(threadName)
        self.toRedirect = toRedirect
        self.node = node
        self.chord = node.chord



    def run(self):
        while not self.stopEvent.isSet():

            try:
                connection, request = self.toRedirect.get(True, 1)

                id = int(request[1].id.decode())

                if id < 0 or id >= (1 << self.node.mBits):
                    self.return_not_found(connection)
                    continue

                responsible_server_id = self.node.fromID(id)

                print("Responsable for", id, "is the node", responsible_server_id)

                stub = self.chord.search_by_id(responsible_server_id, True)

                request_type = request[0]
                if request_type == 'READ':
                    result = stub.read.future(request[1])
                elif request_type == 'CREATE':
                    result = stub.create.future(request[1])
                elif request_type == 'UPDATE':
                    result = stub.update.future(request[1])
                else:
                    result = stub.delete.future(request[1])

                result.add_done_callback(get_response_handler(connection))

            except Empty:
                continue

        print("Exiting Redirector")
        self.stopEvent.clear()
        self.stopFinish.set()

    def return_not_found(self, connection):
        connection.put(StatusCode.OUT_OF_RANGE)


def get_response_handler(_connection):
    def response_handler(response, connection=_connection):
        try:
            r = response.result()
            connection.put(r)
        except Exception as e:
            connection.put(e.code())
    return response_handler