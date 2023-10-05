/*
These functions handle parsing the chord-pro text format
*/


function parseChordProFormat(chordProLinesArray, count) {
  //parse the song lines with embedded
  //chord pro chords and add them to DOM
  console.log('parseChordProFormat::chordProLinesArray')
  console.dir(chordProLinesArray)
  
  //add the lines of text to html <p> elements
  let textDiv = document.getElementById("text-area")
  textDiv.innerHTML = '' //clear the html
 
  let chordLine = ''
  let lyricLine = ''
  
  for (let i = 0; i < chordProLinesArray.length; i++) {
    let line = chordProLinesArray[i]
    
    let isReadingChord = false
    chordLine = ''
    lyricLine = ''
    let chordLength = 0 //length of chord symbol

    for (let charIndex = 0; charIndex < line.length; charIndex++) {
      let ch = line.charAt(charIndex)
      if (ch === '[') {
        isReadingChord = true
        if(chordLength > 0){
          //put a blank between tighly spaced chords
          chordLine += ' '
          chordLength ++
        }
      }
      if (ch === ']') {
        isReadingChord = false
      }
      if (!isReadingChord && ch != ']') {
        lyricLine = lyricLine + ch
        if (chordLength > 0) chordLength-- //consume chord symbol char
        else chordLine = chordLine + ' '  //pad chord line with blank
      }
      if (isReadingChord && ch != '[') {
        chordLine = chordLine + ch
        chordLength++
      }
    }
    if(count === 0){
      if(chordLine.trim() !== ''){
      textDiv.innerHTML = textDiv.innerHTML + `<pre><span class="chord" >${chordLine}</span></pre>` 
      }
      if(lyricLine.trim() !== ''){
        textDiv.innerHTML = textDiv.innerHTML + `<pre>${lyricLine}</pre>`
      }
    }else if(count > 1 || count < 12 || count <= -1){
      if(chordLine.trim() !== ''){
        textDiv.innerHTML = textDiv.innerHTML + `<pre><span class="chordRed">${chordLine}</span></pre>` 
        }
        if(lyricLine.trim() !== ''){
          textDiv.innerHTML = textDiv.innerHTML + `<pre>${lyricLine}</pre>`
        }
    }
    
    
  }

}
