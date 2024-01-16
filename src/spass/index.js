const http = require('http')

const doOptions = res => {
  res.writeHead(200, {
    'Content-Type': 'text/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': '*'
  })
}

const init = () => {
  http.createServer((req, res) => {
    console.log(req.method)
    if (req.method === 'OPTIONS') {
      doOptions(res)
    }

    res.end()
  }).listen(9092)
}

module.exports = {
  init: init
}
