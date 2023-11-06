//connect to server and retain the socket
//connect to same host that served the document

//const socket = io('http://' + window.document.location.host)
const socket = io() //by default connects to same server that served the page
let permission = 0
let firstTime = 1
let currentUser
socket.on('serverSays', function(message, user, receivingUser, groupUser) {
  let msgDiv = document.createElement('div')
  let actualMsg = ''

  msgDiv.textContent = message
  if (firstTime === 1){
    document.getElementById('messages').appendChild(msgDiv)
    firstTime = -1
  }else if(permission === 1 ){
      
     
    msgDiv.textContent = user + ": " + message
    //check if there's multiple users and if the current user is in the list
    if (groupUser.length !== 0 && (groupUser.includes(currentUser) || user === currentUser)){ 
      
      msgDiv.textContent = message + " (from " + user + ")"
      msgDiv.style.backgroundColor = 'red'
      document.getElementById('messages').appendChild(msgDiv)
    }
    //check if the receiving user matches with the current user
    else if (receivingUser !== '' && (receivingUser === currentUser || user === currentUser)){
      actualMsg = message.substring(message.indexOf(":")+1)
      msgDiv.textContent = user + " to " + receivingUser + ":" + actualMsg
      msgDiv.style.backgroundColor = 'red'
      document.getElementById('messages').appendChild(msgDiv)
    }
    else if (currentUser === user){ //blue msg box for sender 
      msgDiv.style.backgroundColor = 'lightblue'
      
    }else{ //grey box for other's 
      msgDiv.style.backgroundColor = '#e8e8e8'
      
    }
    //display when no user's sending msg to each other 
    if (receivingUser === '' && groupUser.length === 0){  
      document.getElementById('messages').appendChild(msgDiv)
    }
    
  }
  
  
})

function sendMessage() {
  if (permission === 0 ) return //do nothing if user hasn't enter their name

  let message = document.getElementById('msgBox').value.trim()
  if(message === '') return //do nothing
  //message = currentUser +": " + message
  socket.emit('clientSays', message, currentUser)
  
  document.getElementById('msgBox').value = ''
}

function addcurrentUser(){
  currentUser = document.getElementById('userNameBox').value
  let button = document.getElementById('userNameButton')
  let msgDiv = document.getElementById('messages')
 
  if (currentUser !== ''){ //check for blank space
    if (RegExp(/^\p{L}/,'u').test(currentUser[0])){ //check for first character as letter
      if (/^[A-Za-z0-9]*$/.test(currentUser)){ //check whole name
        permission = 1 //give permission to user to use send messages
        button.disabled = true //disabled button once user has already registered
        msgDiv.innerHTML = msgDiv.innerHTML + `<p> ${"You've successfully registered"}<p>`

        socket.emit('clientSaysUserName', currentUser) //send user's name to server
        
      }else{
        document.getElementById('currentUser').value = ''
      }
      

    }else{
    document.getElementById('currentUser').value = ''
    }
    
  }
}

function clear(){
  let msgDiv = document.getElementById('messages')
  let divContent = msgDiv.querySelectorAll('div')
  let size = divContent.length

  for (let i = 1; i < size; i++){
    let msgBox = msgDiv.getElementsByTagName('div')[i]
    msgBox.style.display = 'none'
  }
}

function handleKeyDown(event) {
  const ENTER_KEY = 13 //keycode for enter key
  if (event.keyCode === ENTER_KEY) {
    
    sendMessage()
    return false //don't propogate event
  }
}

//Add event listeners
document.addEventListener('DOMContentLoaded', function() {
  //This function is called after the browser has loaded the web page

  //add listener to buttons
  document.getElementById('send_button').addEventListener('click', sendMessage)

  //listner for add user name button
  document.getElementById('userNameButton').addEventListener('click', addcurrentUser)

  //listner for clear button
  document.getElementById('clear').addEventListener('click', clear)

  //add keyboard handler for the document as a whole, not separate elements.
  document.addEventListener('keydown', handleKeyDown)
  //document.addEventListener('keyup', handleKeyUp)
})
