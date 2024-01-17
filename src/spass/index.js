const http = require('http')

const doOptions = res => {
  res.writeHead(200, {
    'Content-Type': 'text/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': '*'
  })
  res.end()
}

const getDataFilename = () => {
  const dirName = `${process.env.HOME}/.config/spass`
  const filename = `${dirName}/data`
  return {dirName, filename}
}

const save = body => {
  if (body === null || body === undefined || body.length === 0) return

  const obj = JSON.parse(body)
  const fs = require('fs')
  const {dirName, filename} = getDataFilename()

  try {
    fs.mkdirSync(dirName, {recursive: true})
  } catch {}

  let data = 'module.exports = {\n'

  for (let k in obj) {
    data += `  ${JSON.stringify(k)}: ${JSON.stringify(obj[k])},\n`
  }

  data += '}'
  fs.writeFileSync(filename, data)
}

const doPost = (req, res) => {
  let body = ''
  req.on('readable', () => {
    const chunk = req.read()
    body += chunk !== null ? chunk : ''
  })
  req.on('end', () => {
    save(body)
    res.writeHead(200, {
      'Content-Type': 'text/json',
      'Access-Control-Allow-Origin': '*'
    })
    res.end()
  })
}

doGet = (req, res) => {
  if (req.url === '/data/') {
    const {filename} = getDataFilename()
    const data = require(filename)
    res.writeHead(200, {
      'Content-Type': 'text/json',
      'Access-Control-Allow-Origin': '*'
    })
    res.write(JSON.stringify(data))
    res.end()
  }
}

const init = () => {
  http.createServer((req, res) => {
    if (req.method === 'OPTIONS') {
      doOptions(res)
    } else if (req.method === 'POST') {
      doPost(req, res)
    } else if (req.method === 'GET') {
      doGet(req, res)
    }

  }).listen(9092)
}

module.exports = {
  init: init
}
