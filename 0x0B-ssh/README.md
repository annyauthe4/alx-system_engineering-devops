##OVERVIEW
  A secure shell (SSH) project on SysAdmin DevOps network project
  It includes connecting to a remote server using rsa key pair generation
  which includes a public key and a private key

## TO CONNECT TO A WEB SERVER USING A PRIVATE KEY
  ssh -i private/key/file/path server-name@ip-address.

## TO CREATE AN RSA KEY PAIR WITH A PRIVATE KEY
  ssh-keygen -t rsa -b 4096 -f school -N betty

  The -t flag implies the type of ssh to generate
  The -b flag for the number of bytes
  The -f flag indicates the filename where the private key is stored
  The -N flag is the passphrase to be used when login in

There is a file ~/.ssh/known_hosts. It stores the public keys of allowed clients on the server
