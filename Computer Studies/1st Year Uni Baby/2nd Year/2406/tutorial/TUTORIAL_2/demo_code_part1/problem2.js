function landscape() {
    let result = ""
  
    function flat(size) {
     
      for (let count = 0; count < size; count++){
        result += "_"
      }
        
    }
  
    function hill(size) {
        result += "/"
      for (let count = 0; count < size; count++)
        result += " "
        result += "\\"
    }

    function mountain(size){
        result += "/"
        
        for (let count = 0; count < size; count++)
            result += " "
            result += "  \\"       
    }
    //BUILD SCRIPT
    flat(3)
    mountain(3)
    console.log("     ___")
    console.log("    /   \\    /\\      _")
    flat(2)
    mountain(0)
    flat(4)
    
    hill(1)
    flat(1)
    
    //END SCRIPT
    return result
  
  }
  
  
  console.log(landscape())