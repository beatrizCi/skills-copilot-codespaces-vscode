// Create web server
const express = require('express');
const app = express();
// Create server
const http = require('http');
const server = http.createServer(app);
// Create socket.io instance
const io = require('socket.io')(server);
