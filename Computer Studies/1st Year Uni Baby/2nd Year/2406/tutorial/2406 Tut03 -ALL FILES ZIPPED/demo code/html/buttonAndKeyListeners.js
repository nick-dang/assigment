//KEY CODES
//should clean up these hard-coded key codes
const ENTER = 13
const RIGHT_ARROW = 39
const LEFT_ARROW = 37
const UP_ARROW = 38
const DOWN_ARROW = 40


function handleKeyDown(e) {

  //console.log("keydown code = " + e.which)

  let dXY = 5; //amount to move in both X and Y direction
  if (e.which == UP_ARROW && movingBox.y >= dXY)
    movingBox.y -= dXY //up arrow
  if (e.which == RIGHT_ARROW && movingBox.x + movingBox.width + dXY <= canvas.width)
    movingBox.x += dXY //right arrow
  if (e.which == LEFT_ARROW && movingBox.x >= dXY)
    movingBox.x -= dXY //left arrow
  if (e.which == DOWN_ARROW && movingBox.y + movingBox.height + dXY <= canvas.height)
    movingBox.y += dXY //down arrow

  let keyCode = e.which
  if (keyCode == UP_ARROW | keyCode == DOWN_ARROW) {
    //prevent browser from using these with text input drop downs
    e.stopPropagation()
    e.preventDefault()
  }

}

function handleKeyUp(e) {
//  console.log("key UP: " + e.which)
  if (e.which == RIGHT_ARROW | e.which == LEFT_ARROW | e.which == UP_ARROW | e.which == DOWN_ARROW) {
    let dataObj = {
      x: movingBox.x,
      y: movingBox.y
    }
    //create a JSON string representation of the data object
    let jsonString = JSON.stringify(dataObj)
    //DO NOTHING WITH THIS DATA FOR NOW


  }
  if (e.which == ENTER) {
    handleSubmitButton() //treat ENTER key like you would a submit
    document.getElementById('userTextField').value = ''

  }

  e.stopPropagation()
  e.preventDefault()

}


function handleSubmitButton() {

  let userText = document.getElementById('userTextField').value
  if (userText && userText != '') {

    let textDiv = document.getElementById("text-area")
    textDiv.innerHTML = textDiv.innerHTML + `<p> ${userText}</p>`    


    let userRequestObj = {text: userText}
    let userRequestJSON = JSON.stringify(userRequestObj)
    document.getElementById('userTextField').value = ''
    //alert ("You typed: " + userText);

    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log("data: " + this.responseText)
        console.log("typeof: " + typeof this.responseText)
        //we are expecting the response text to be a JSON string
        let responseObj = JSON.parse(this.responseText)
        
        song = responseObj.songLines
        
        
        if(responseObj.text === "NOT FOUND: " + userText){
          movingString.word = responseObj.text
        }else{
          movingString.word = "FOUND"
          let line = ''
          let ch = ''
          let word_store = []
          for (let i = 0; i < song.length; i++){
            line = song[i]
            let space_index = 0
            let start_index = 0
            
            for (let j = 0; j < line.length; j++){

              ch = line.charAt(j)
              if (ch === ' '){
                space_index = j
                word_store.push(line.substring(start_index, space_index))
                start_index = j+1
              }else if(j === line.length - 1){
                word_store.push(line.substring(start_index))
                
              }
            }
          }
          set_words(word_store)
          randomizeWordLocation()

        }

        drawCanvas()
      }

    }
    xhttp.open("POST", "userText") //API .open(METHOD, URL)
    xhttp.send(userRequestJSON) //API .send(BODY)
  }
}


function handleSubmitButtonWithFetch(){
  let userText = document.getElementById('userTextField').value
  if (userText && userText != ''){
    let userRequestObj = { text: userText}
    let textDiv = document.getElementById("text-area")
    textDiv.innerHTML = textDiv.innerHTML + `<p> ${userText}</p>` 
  
    fetch('userText', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userRequestObj),
      
    })
    .then((response) => response.json())
      
    .then((data) => {
      document.getElementById('userTextField').value = ''
      song = data.songLines
        
      console.log("data: " + JSON.stringify(data))
      console.log("typeof: " + typeof JSON.stringify(data))
      if(data.text === "NOT FOUND: " + userText){
        movingString.word = data.text
      }else{
        movingString.word = "FOUND"
        let line = ''
        let ch = ''
        let word_store = []
        for (let i = 0; i < song.length; i++){
          line = song[i]
          let space_index = 0
          let start_index = 0
          
          for (let j = 0; j < line.length; j++){

            ch = line.charAt(j)
            if (ch === ' '){
              space_index = j
              word_store.push(line.substring(start_index, space_index))
              start_index = j+1
            }else if(j === line.length - 1){
              word_store.push(line.substring(start_index))
              
            }
          }
        }
        set_words(word_store)
      }
      drawCanvas()
     
    })
    .catch((error) => {
      console.error('ERROR:', error)
    })
  }
 

  
}