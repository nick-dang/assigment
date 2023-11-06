/*
Example of a "static server implemented with the express framework
and express.js static Middleware.

PREREQUISITES:
install express module using the package.json file with command:
>npm install

TO TEST:
Use browser to view pages at http://localhost:3000/index.html.
*/
const express = require('express')
const app = express()
const logger = require('morgan') //request logger

const PORT = process.env.PORT || 3000
const ROOT_DIR = '/public' //root directory for our static pages

//Middleware
app.use(function(req, res, next) {
  console.log('-------------------------------')
  console.log('req.path: ', req.path)
  console.log('serving:' + __dirname + ROOT_DIR + req.path)
  next() //allow next route or middleware to run
})

//use morgan logger to keep request log files
app.use(logger('dev'))

app.use(express.static(__dirname + ROOT_DIR)) //provide static server



app.use((req,res)=>{
  res.status(404).send('404: OOPS YOU BROKE THE INTERNET')
})
//Routes



//start server
app.listen(PORT, err => {
  if (err) console.log(err)
  else {
    console.log(`Server listening on port: ${PORT} CNTL-C to Quit`)
    console.log('To Test')
    console.log('http://localhost:3000/greeting.html')
    console.log('http://localhost:3000/index.html')
    console.log('http://localhost:3000/table.html')
    console.log('http://localhost:3000/table_css_internal.html')
    console.log('http://localhost:3000/table_css_external.html')
  }
})
