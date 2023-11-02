//KEY CODES
//should clean up these hard-coded key codes
const ENTER = 13

function handleKeyUp(e) {
  if (e.which == ENTER) {
    handleGetPuzzleButton() //treat ENTER key like you would a submit
    document.getElementById('userTextField').value = ''

  }
  e.stopPropagation()
  e.preventDefault()

}


function handleGetPuzzleButton() {
  let userText = document.getElementById('userTextField').value
  let textDiv = document.getElementById("text-area")

  textDiv.innerHTML = ' ' 
  if (userText && userText != '') {

    textDiv.innerHTML = textDiv.innerHTML + `<p><span class="normalText">${userText}</span></p>`    


    let userRequestObj = {text: userText}
    let userRequestJSON = JSON.stringify(userRequestObj)
    document.getElementById('userTextField').value = ''
  
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        
        //we are expecting the response text to be a JSON string
        let responseObj = JSON.parse(this.responseText)
        
        puzzle = responseObj.puzzleLines
        
        let line = ''
        let ch = ''
        if (responseObj.text !== "NOT FOUND: " + userText){
          
          word_store = []
          for (let i = 0; i < puzzle.length; i++){
            line = puzzle[i]
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

          
          set_words(word_store) //replace the words on the canvas
          
          drawCanvas()
        }
      }
    }
    xhttp.open("POST", "userText") //API .open(METHOD, URL)
    xhttp.send(userRequestJSON) //API .send(BODY)
  }
}


function handleSolvePuzzleButton(){
  alignWords() 
  let textDiv = document.getElementById("text-area")
  textDiv.innerHTML = ' '   
  let current_line = ''
  let ordered_line = sortWord() //get the ordered and aligned word array
  let line = ordered_line[0].y //keep track of each line 
  let index = 0;
  let correct = "correctText";

  //Loop through user's aligned, ordered texts vs texts from server
  //to determined the correct font colour
  while(index !== ordered_line.length){  
      if (ordered_line[index].word !== word_store[index]){
        correct = "wrongText";
        break
      }
      index++
  }
  for (let i = 0; i < ordered_line.length; i++){
    
    if (ordered_line[i].y === line){ //check if current character/word is the same "line" via y axis
      current_line += ordered_line[i].word + ' '
      if ( i === ordered_line.length-1){ 
        textDiv.innerHTML = textDiv.innerHTML + `<p><span class=${correct}>${current_line}</span></p>`
      }
    }else if (ordered_line[i].y !== line ){
      line = ordered_line[i].y //set a new line
      
      textDiv.innerHTML = textDiv.innerHTML + `<p><span class=${correct}>${current_line}</span></p>` //print whenever there's a new line

      current_line = ''
      current_line += ordered_line[i].word + ' '
      if ( i === ordered_line.length-1){ //print if the current character/word is the last one 
        textDiv.innerHTML = textDiv.innerHTML + `<p><span class=${correct}>${current_line}</span></p>`
      }
      
    }
 
  }
 
  drawCanvas()
  
}