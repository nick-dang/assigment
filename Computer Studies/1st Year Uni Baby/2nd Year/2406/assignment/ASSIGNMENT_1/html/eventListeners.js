document.addEventListener('DOMContentLoaded', function() {
  /*
  This is called after the browser
  has loaded the web page
  */

  //add listeners to buttons
  document.getElementById('submit_button').addEventListener('click', handleSubmitButton)

  document.getElementById('transDown').addEventListener('click', handleTransDown)
  document.getElementById('transUp').addEventListener('click', handleTransUp)

  //add key handler for the document as a whole, not separate elements.
  document.addEventListener('keydown', handleKeyDown)
  document.addEventListener('keyup', handleKeyUp)
})
