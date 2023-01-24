Welcome to our simple FTP server and client project using Python!

In this project, we will be using the pyftpdlib library to create a basic FTP server and the ftplib library to create a basic FTP client. The pyftpdlib library is a pure Python FTP server library, while the ftplib library is a library for interacting with FTP servers.
Setting up the FTP server

First, install the pyftpdlib library using pip:

        pip install pyftpdlib

Import the necessary modules from the library:

        from pyftpdlib.authorizers import DummyAuthorizer
        from pyftpdlib.handlers import FTPHandler
        from pyftpdlib.servers import FTPServer

Create an instance of the DummyAuthorizer class to handle user authentication:

        authorizer = DummyAuthorizer()
        authorizer.add_user("user", "password", "path/to/home/directory", perm="elradfmw")

Create an instance of the FTPHandler class and set the authorizer and other options:

        handler = FTPHandler
        handler.authorizer = authorizer
Create an instance of the FTPServer class and start the server:

        server = FTPServer(("127.0.0.1", 2121), handler())
        server.serve_forever()

Setting up the FTP client

First, install the ftplib library using pip:

        pip install ftplib

Import the library:

        import ftplib
Connect to the FTP server using the FTP() function, passing in the server's IP address and port as arguments:

        ftp = ftplib.FTP()
        ftp.connect("server_ip", server_port)

Log in to the server using the login() method, passing in your username and password as arguments:

        ftp.login("username", "password")

