from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

authorizer.add_user("Twarga","123","./Ftp_directory", perm='elradfmwMT')

handler = FTPHandler

handler.authorizer = authorizer
handler.banner = "pyftpdlib based ftpd ready."

server = FTPServer(("127.0.0.1", 2121), handler)
server.serve_forever()
