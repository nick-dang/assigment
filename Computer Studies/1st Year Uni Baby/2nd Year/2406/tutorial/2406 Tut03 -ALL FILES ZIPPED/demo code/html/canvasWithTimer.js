/*
Javascript example using an html <canvas> as the main
app client area.
The application illustrates:
-handling mouse dragging and release
to drag a strings around on the html canvas
-Keyboard arrow keys are used to move a moving box around

Here we are doing all the work with javascript.
(none of the words are HTML, or DOM, elements.
The only DOM element is just the canvas on which
where are drawing and a text field and button where the
user can type data

Mouse event handlers are being added and removed.

Keyboard keyDown handler is being used to move a "moving box" around
Keyboard keyUP handler is used to trigger communication with the
server via POST message sending JSON data

*/

//DATA MODELS
//Use javascript array of objects to represent words and their locations
let words = []

words.push({word: "I", x: 50, y: 50})
words.push({word: "like", x: 70, y: 50})
words.push({word: "javascript", x: 120, y: 50})


//a function to set words
function set_words(words_input){
  for (let i = 0; i < words_input.length; i++){
    
    if(i === words.length){
      words.push({word: words_input[i], x: 50, y: 50})
    }else{
      words[i].word = words_input[i]
    }
  }
  randomizeWordLocation()
}

//represents the word moving around the canvas being
//animated using timer events
let movingString = {
  word: "MOVING WORD",
  x: 100,
  y: 100,
  xDirection: 1, //+1 for leftwards, -1 for rightwards
  yDirection: 1, //+1 for downwards, -1 for upwards
  stringWidth: 50, //will be updated when drawn
  stringHeight: 24 //estimated string height
} //assumed height based on drawing point size

//intended for keyboard control
let movingBox = {
  x: 50,
  y: 50,
  width: 100,
  height: 100
}

let timer //used for the motion animation

const canvas = document.getElementById('canvas1') //our drawing canvas

function getWordAtLocation(aCanvasX, aCanvasY) {

  //locate the word near aCanvasX,aCanvasY
  //Just use crude region for now.
  //should be improved to using length of word etc.

  //note you will have to click near the start of the word
  //as it is implemented now
  let TOLERANCE = 0;
  const height = 20
  const context = canvas.getContext('2d')
  
  
  for (let i = 0; i < words.length; i++) {
    TOLERANCE = context.measureText(words[i].word).width

    if (Math.abs(aCanvasX - words[i].x) < TOLERANCE && (aCanvasY > words[i].y-height && aCanvasY < words[i].y )){
      console.log("x:" + words[i].x + ", y:" + words[i].y )
      console.log(TOLERANCE)
      return words[i]
    }  
    
  }
  return null
}

function randomizeWordLocation(){
  for (let i = 0; i < words.length; i++){
    
    let random_loc_wid = Math.floor(Math.random()*canvas.width)
    let random_loc_hei = Math.floor(Math.random()*canvas.height)
    if(random_loc_hei === canvas.height){
      random_loc_hei = canvas.height - 10
    }else if (random_loc_hei < 30){
      random_loc_hei = 30
    }
    if (random_loc_wid > (canvas.width - 120)){
      random_loc_wid = canvas.width - 120
    }
    words[i].x = random_loc_wid
    words[i].y = random_loc_hei
    
  }
}
randomizeWordLocation()

function drawCanvas() {
  
  /*
  Call this function whenever the canvas needs to be redrawn.
  */
  
  const context = canvas.getContext('2d')

  context.fillStyle = 'white'
  context.fillRect(0, 0, canvas.width, canvas.height) //erase canvas

  context.font = '20pt Arial'
  context.fillStyle = 'cornflowerblue'
  context.strokeStyle = 'blue'

  for (let i = 0; i < words.length; i++) {
    
    let data = words[i]
    context.fillText(data.word, data.x, data.y)
    context.strokeText(data.word, data.x, data.y)

  }

  movingString.stringWidth = context.measureText(movingString.word).width
  //console.log(movingString.stringWidth)
  context.fillText(movingString.word, movingString.x, movingString.y)

  //draw moving box
  context.fillRect(movingBox.x,
    movingBox.y,
    movingBox.width,
    movingBox.height)

  //draw circle
  context.beginPath();
  context.arc(canvas.width / 2, //x co-ord
    canvas.height / 2, //y co-ord
    canvas.height / 2 - 5, //radius
    0, //start angle
    2 * Math.PI //end angle
  )
  context.stroke()
}
