# ANDS pubsub notification system

For use in Data Source Settings screen

## Requirements
* redis installed and running
* node >8

## Installation 
```
yarn install
```

## Configuration
Copy `.env.example` to `.env` and make the necessary changes
```
MODE=HTTP
PORT=3000
SSL_KEY=
SSL_CERT=%
```

Add the following block to Apache vhost file
```
# socket.io pubsub
RewriteEngine On
RewriteCond %{REQUEST_URI}  ^/socket.io            [NC]
RewriteCond %{QUERY_STRING} transport=websocket    [NC]
RewriteRule /(.*)           ws://localhost:3000/$1 [P,L]
ProxyPass /socket.io http://localhost:3000/socket.io
ProxyPassReverse /socket.io http://localhost:3000/socket.io
```
and modify the RDA Registry `SOCKET_URL` with
```
SOCKET_URL="https://localhost/"
```

## Run
```
node server.js
```

## Run with pm2
```
npm install -g pm2
pm2 start server.js
```

## Upgrade node version
Standard installation of RHEL and CentOS comes with `node v6` when `yum install nodejs`. To upgrade node it's recommended to use `n` or `nvm`

Using `n` to upgrade `node` to the latest stable version
```
npm install -g npm
npm install -g n
n stable
```