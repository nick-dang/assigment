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
  words = []
  for (let i = 0; i < words_input.length; i++){
    words.push({word: words_input[i], x: 50, y: 50})
    
  }
  
  randomizeWordLocation()
}


let timer //used for the motion animation

const canvas = document.getElementById('canvas1') //our drawing canvas

function getWordAtLocation(aCanvasX, aCanvasY) {
  let TOLERANCE = 0;
  const height = 20
  const context = canvas.getContext('2d')

  for (let i = 0; i < words.length; i++) {
    TOLERANCE = context.measureText(words[i].word).width
    
    if ((aCanvasX > words[i].x && aCanvasX < (words[i].x + TOLERANCE)) && (aCanvasY > words[i].y-height && aCanvasY < words[i].y )){
      
      return words[i]
    }  
    
  }
  return null
}


//get each word location on the canvas
function alignWords(){
  num_of_line = []

  words.sort(function(a,b) {return a.y - b.y}) //sort the words by its y value from smallest to biggest
  let smallest = words[0]
  num_of_line.push({line: smallest.y}) //keep track number of appeared words per line
  
  for (let i = 0; i < words.length; i++){
   if (words[i] !== smallest){
    if (words[i].y < smallest.y+30 && words[i].y > smallest.y-30){
      words[i].y = smallest.y
      
    }else{ // if next word isn't within range, then it's a new line 
      smallest = words[i]

      num_of_line.push({line: smallest.y}) //keep track the y axis as an indicator of a new line
    }
   } 
    //console.log(words[i].word + ", x: " + words[i].x + ", y: ", words[i].y)
  //  console.log(num_of_line[index].line + ", num: " + num_of_line[index].num)
  }
  
}


function sortWord(){
  let index = 0 
  let ordered_line = []
  let store_line = []
 
  for (let i = 0; i < words.length; i++){ 
    if (words[i].y === num_of_line[index].line){
      store_line.push(words[i])
    }else{
      
      store_line.sort(function(a,b) {return a.x - b.x})
      
      ordered_line = ordered_line.concat(store_line)
      
      store_line.length = 0
      //console.log(ordered_line)
      store_line.push(words[i])

      index++
    }
    if(i === words.length-1){
        store_line.sort(function(a,b) {return a.x - b.x})
        ordered_line = ordered_line.concat(store_line) //add the line-word into array
      }

  }
  
  return ordered_line
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


  context.stroke()
}
