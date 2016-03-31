# Socket Programming with Edison
We would like to communicate with Intel Edison wirelessly so we setup the Edison as a server and commincate with it using TCP. 

### Running network
On the server side you only need to call the tcp_server file
> python tcp_server.py

On the client side you need call the file along with the host name and port number, as follows
> python tcp_client.py hostname port

### Task List
- [ ] Use socketServer class for easier management
- [ ] Use threads for non-blocking execution  
