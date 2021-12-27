# Client-Server Model

- client
  - a machine or process that requests data or service from a server
    - single piece of software/machine can be both client and a server at the same
      time
- server
  - a machine or process that provides data or service for a client, usually by
    listening for incoming network calls
- Client-Server Model
  - a paradigm by which modern systems are designed which consists of clients
    requesting data or service from servers and servers providing data or service
    to clients
- IP Address
  - any address given to each machine connected to the public internet. IPv4 addresses consist of four numbers separated by dots: **a.b.c.d** where all four numbers are between 0 and 255
  - special values:
    - 127.0.0.1 - localhost
    - 192.168.x.y - your private network
- Port
  - in order for multiple programs to listen to new network connections on the same machine without colliding, they pick a port to listen on. A port is an integer between 0 and 65,535 (2^16 total ports)
    - ports 0-1023 are system ports (well-known ports) and shouldn't be used by user-level processes
    - predefined use port examples
      - 22: secure shell
      - 53: DNS lookup
      - 80: HTTP
      - 443: HTTPS
- DNS
  - domain name system, it describes entities and protocols involved in the translation from domain names to IP addresses. Typically, machines make a DNS query to a well known entity which is responsible for returning the IP address (or multiple ones) of the requested domain in the response
