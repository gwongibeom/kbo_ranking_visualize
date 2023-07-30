const express = require('express')
const app = express()

app.set('view engine', 'ejs');

app.use('/static', express.static('static'))

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html')
})

app.get('/robots.txt', (req, res) => {
    res.type("text/plain")
    res.send(
        `User-agent: *\nAllow: /\n`
    )
})

app.get('/detail/:year/:month/:day', function (req, res) {
    const paramsYear = req.params.year
    const paramsMonth = req.params.month
    const paramsDay = req.params.day
    res.render("detail",{ year: paramsYear, month: paramsMonth, day: paramsDay})
})

app.use((req, res, next) => {
    res.status(404).sendFile(__dirname + '/404.html')
})

app.listen(4000, () => {
    console.log(`🏄 ride on port 4000`)
})
