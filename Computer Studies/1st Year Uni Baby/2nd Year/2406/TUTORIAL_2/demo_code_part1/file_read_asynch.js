
/*
Example of ASYNCHRONOUS file read.
Function readFile does not block (wait) for the file to be read.

Instead its argument function(err,data) will be called once the file has been read.
function(err,data) is the "call back" function that will be called when readFile's task is done.

Notice "DONE" gets written to the console before the file contents. Make
sure you understand why that is.
*/


const fs = require('fs')

fs.readFile('songs/sister_golden_hair.txt', function(err, data) {
  if(err) throw err
  let array = data.toString().split("\n") //keep lyrics
  const regex = /\[([^\]]+)\]/g;
  const chordsToRemove = ["[E]", "[G#min]", "[A]", "[C#min]", "[F#min]", "[Esus2]"] //array to search through to remove the chords from the lyrics
  let chords = []; //keep the chords
  let match; 
  
  while ((match = regex.exec(array))) { //remove the chords and put into an array
    chords.push(match[1]);
  }

  for (let i = 0; i < array.length; i++){ // a loop to remove the chords from the lyrics
    for (let j = 0; j < chordsToRemove.length; j++){
      array[i] = array[i].replaceAll(chordsToRemove[j], "")
    }
  }
  
  let index = 0;
  let track = 0;
  for (let line of array){
    
    for (let i = track; i < chords.length; i++){
      if (index === 2){
        console.log("\t" + chords[i] + "\t\t\t     " + chords[i+1])
        track = i+2;
        break;
      }else if(index === 3){
        console.log("\t" + chords[i] + "\t\t" + chords[i+1] + "\t     " + chords[i+2])
        track = i+3;
        break;
      }else if(index === 4){
        console.log("\t\t\t\t   " + chords[i] + " " + chords[i+1] + "\t    " + chords[i+2])
        track = i+3
        break;
      }else if(index === 5){
        console.log("       " + chords[i] + "\t      " + chords[i+1] + "\t\t     " + chords[i+2] + "\t  " + chords[i+3] +"\t" + chords[i+4])
        
        break;
      }
      else{
        break;
      }
    }
    console.log(line)
    index++
  }

  })
console.log("DONE")
