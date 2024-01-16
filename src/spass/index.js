const http = require('http')

const init = () => {
  http.createServer((req, res) => {
    console.log(req)
  }).listen(9092)
}

module.exports = {
  init: init
}
