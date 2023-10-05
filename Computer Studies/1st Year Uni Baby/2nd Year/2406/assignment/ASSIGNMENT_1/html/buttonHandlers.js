//KEY CODES
//should clean up these hard coded key codes
const ENTER = 13
const RIGHT_ARROW = 39
const LEFT_ARROW = 37
const UP_ARROW = 38
const DOWN_ARROW = 40


function handleKeyDown(e) {

  //console.log("keydown code = " + e.which );
  let keyCode = e.which
  if (keyCode == UP_ARROW | keyCode == DOWN_ARROW) {
    //prevent browser from using these with text input drop downs
    e.stopPropagation()
    e.preventDefault()
  }

}

function handleKeyUp(e) {
  //console.log("key UP: " + e.which);
  if (e.which == RIGHT_ARROW | e.which == LEFT_ARROW | e.which == UP_ARROW | e.which == DOWN_ARROW) {
    //do nothing for now
  }

  if (e.which == ENTER) {
    handleSubmitButton() //treat ENTER key like you would a submit

    document.getElementById('userTextField').value = ''
  }

  e.stopPropagation()
  e.preventDefault()

}

function handleSubmitButton() {

  //get text from user text input field
  let userText = document.getElementById('userTextField').value
  //clear lines of text in textDiv
  let textDiv = document.getElementById("text-area")
  textDiv.innerHTML = ''

  if (userText && userText !== '') {
    let userRequestObj = {
      text: userText
    }
    let userRequestJSON = JSON.stringify(userRequestObj)
    //clear the user text field
    document.getElementById('userTextField').value = ''
    //alert ("You typed: " + userText);

    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
       console.log("typeof: " + typeof this.responseText)
       console.dir(this.responseText)
       //we are expecting the response text to be a JSON string
       let responseObj = JSON.parse(this.responseText)
       console.dir(responseObj)
        
        words = [] //clear drag-able words array;
        if (responseObj.songLines) {
          song.songLines = responseObj.songLines
          transposedByNSemitones = 0 //reset transpose to no-transpose
          parseChordProFormat(song.songLines, transposedByNSemitones)
        }

      }
    }
    xhttp.open("POST", "song") //API .open(METHOD, URL)
    xhttp.send(userRequestJSON) //API .send(BODY)

  }

}

function handleTransUp(){
  List_of_chords = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
  AltList_of_chords = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
  transposedByNSemitones++
  if (transposedByNSemitones >= 12){
    transposedByNSemitones = 0
  }
  let lyricLine1 = []
  let lyricLine2 = ''
  for (let i = 0; i <song.songLines.length; i++){
    let line = song.songLines[i]
    lyricLine2 = ''
    let read = false

    for (let j = 0; j < line.length; j++){
      let ch = line.charAt(j)
      let twoCh = line.charAt(j-1) + line.charAt(j)
      lyricLine2 += ch
      if (line.charAt(j+1) === '#' || line.charAt(j+1) === 'b'){
        continue
      }
      if (ch === '['){
        read = true;
      }
      if (read && ch !== ']'){
        if(twoCh === 'G#' || twoCh === 'Ab'){
          lyricLine2 = lyricLine2.substring(0, lyricLine2.length-2) +  'A'
        }else if(List_of_chords.includes(twoCh)){
          lyricLine2 = lyricLine2.substring(0, lyricLine2.length-2) +  List_of_chords[List_of_chords.indexOf(twoCh)+1]
        }else if(AltList_of_chords.includes(twoCh)){
          lyricLine2 = lyricLine2.substring(0, lyricLine2.length-2) +  AltList_of_chords[AltList_of_chords.indexOf(twoCh)+1]
        }else if(List_of_chords.includes(ch)){
          lyricLine2 = lyricLine2.substring(0, lyricLine2.length-1) +  List_of_chords[List_of_chords.indexOf(ch)+1]
        }

      }else {
        read = false
      }
    }
    lyricLine1.push(lyricLine2)
  }
  song.songLines = lyricLine1
  parseChordProFormat(song.songLines,transposedByNSemitones)
}

function handleTransDown(){
  let lyricLine1 = []
  let lyricLine2 = ''
  transposedByNSemitones--
  if (transposedByNSemitones == -12){
    transposedByNSemitones = 0
  }
  for (let i = 0; i <song.songLines.length; i++){
    let line = song.songLines[i]
    lyricLine2 = ''
    let read = false

    for (let j = 0; j < line.length; j++){
      let ch = line.charAt(j)
      let twoCh = line.charAt(j-1) + line.charAt(j)
      lyricLine2 += ch
      if (line.charAt(j+1) === '#'){
        continue
      }
      if (ch === '['){
        read = true;
      }
      if (read && ch !== ']'){
        if(List_of_chords.includes(twoCh)){
          lyricLine2 = lyricLine2.substring(0, lyricLine2.length-2) +  List_of_chords[List_of_chords.indexOf(twoCh)-1]
        }else if(AltList_of_chords.includes(twoCh)){
          lyricLine2 = lyricLine2.substring(0, lyricLine2.length-2) +  AltList_of_chords[AltList_of_chords.indexOf(twoCh)-1]
        }
        else if(ch === 'A'){
          lyricLine2 = lyricLine2.substring(0, lyricLine2.length-1) +  'G#'
        }else if(List_of_chords.includes(ch)){
          lyricLine2 = lyricLine2.substring(0, lyricLine2.length-1) +  List_of_chords[List_of_chords.indexOf(ch)-1]
        }

      }else {
        read = false
      }
    }
    lyricLine1.push(lyricLine2)
  }
  song.songLines = lyricLine1
  parseChordProFormat(song.songLines, transposedByNSemitones)
}