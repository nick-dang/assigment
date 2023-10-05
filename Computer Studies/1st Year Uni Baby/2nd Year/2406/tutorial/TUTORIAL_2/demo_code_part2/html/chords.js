/*
These functions handle parsing the chord-pro text format
*/

function parseChordProFormat(chordProLinesArray) {
  //parse the song lines with embedded
  //chord pro chords and add them to DOM

  console.log('type of input: ' + typeof chordProLinesArray)

  //add the lines of text to html <p> elements
  let textDiv = document.getElementById("text-area")
  textDiv.innerHTML = '' //clear the html
  let line = " "
  const regex = /\[([^\]]+)\]/g;
  let chords = []; //keep the chords
  let match; 
  while ((match = regex.exec(chordProLinesArray))) { //remove the chords and put into an array
    chords.push(match[0]);
  }

  for (let i = 0; i < chordProLinesArray.length; i++) {
    line = chordProLinesArray[i]
    
    for (let j = 0; j <chords.length; j++){ //go through the chords arrays
      if (line.includes(chords[j])){ //if a chord is in the line, replace every chord with one that's coloured
        line = line.replaceAll(chords[j], `<span class="chord">${chords[j]}</span>` )
      }
    }
    
  
    console.log(line)
    
    textDiv.innerHTML = textDiv.innerHTML + `<p> ${line}</p>`
  }

  

}
