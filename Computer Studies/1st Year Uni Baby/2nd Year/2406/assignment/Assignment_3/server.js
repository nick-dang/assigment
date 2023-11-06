const server = require('http').createServer(handler)
const io = require('socket.io')(server) //wrap server app in socket io capability
const fs = require('fs') //file system to server static files
const url = require('url'); //to parse url strings
const PORT = process.argv[2] || process.env.PORT || 3000 //useful if you want to specify port through environment variable
                                                         //or command-line arguments

const ROOT_DIR = 'html' //dir to serve static files from
let user = []
const MIME_TYPES = {
  'css': 'text/css',
  'gif': 'image/gif',
  'htm': 'text/html',
  'html': 'text/html',
  'ico': 'image/x-icon',
  'jpeg': 'image/jpeg',
  'jpg': 'image/jpeg',
  'js': 'application/javascript',
  'json': 'application/json',
  'png': 'image/png',
  'svg': 'image/svg+xml',
  'txt': 'text/plain'
}

function get_mime(filename) {
  for (let ext in MIME_TYPES) {
    if (filename.indexOf(ext, filename.length - ext.length) !== -1) {
      return MIME_TYPES[ext]
    }
  }
  return MIME_TYPES['txt']
}

server.listen(PORT) //start http server listening on PORT

function handler(request, response) {
  //handler for http server requests including static files
  let urlObj = url.parse(request.url, true, false)
  console.log('\n============================')
  console.log("PATHNAME: " + urlObj.pathname)
  console.log("REQUEST: " + ROOT_DIR + urlObj.pathname)
  console.log("METHOD: " + request.method)

  let filePath = ROOT_DIR + urlObj.pathname
  if (urlObj.pathname === '/') filePath = ROOT_DIR + '/index.html'

  fs.readFile(filePath, function(err, data) {
    if (err) {
      //report error to console
      console.log('ERROR: ' + JSON.stringify(err))
      //respond with not found 404 to client
      response.writeHead(404);
      response.end(JSON.stringify(err))
      return
    }
    response.writeHead(200, {
      'Content-Type': get_mime(filePath)
    })
    response.end(data)
  })

}

//Socket Server
io.on('connection', function(socket) {
  console.log('client connected')
  //console.dir(socket)

  socket.emit('serverSays', 'You are connected to CHAT SERVER')
  
  socket.on('clientSaysUserName', function(data){ 
    user.push(data)
    
    //show the server's user list
    //console.log(user) 
  
  })

  socket.on('clientSays', function(data, name) {
      console.log('RECEIVED: ' + data + " by " + name)
      let anotherUser = ''
      let groupUser = []
      
      if (data.indexOf(":") > 0){ //check if msg is send to another user
        if (data.indexOf(",") < data.indexOf(":") && data.indexOf(",") !== -1){ //if there's comma
          let nameArray = data.split(/[:,]/) //split wherever there's ':' or ','
          for (let i = 0; i < nameArray.length-1; i++){ //loop over names only

            let trimmedName = nameArray[i].trim() //trim white spaces
            if (user.includes(trimmedName) === false){ //if one of the users isn't in the server's user list
              groupUser = []
              break
            }
            if(trimmedName !== ""){
              groupUser.push(trimmedName)
            }
          }
        }else{
          anotherUser = data.substring(0, data.indexOf(":")) //get user's name
          if(user.includes(anotherUser) === false){ //check if the receiving user is in user list
            anotherUser = ''
          }
        }
      }

      
      //to broadcast message to everyone including sender:
      io.emit('serverSays', data, name, anotherUser, groupUser) //broadcast to everyone including sender
      
      
  })
  

  socket.on('disconnect', function(data) {
    //event emitted when a client disconnects
    console.log('client disconnected')
  })
})

console.log(`Server Running at port ${PORT}  CNTL-C to quit`)
console.log(`To Test:`)
console.log(`Open several browsers to: http://localhost:${PORT}/chatClient.html`)
