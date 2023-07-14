const express = require('express')
const app = express()


app.use('/', express.static('static'))

app.get('/',(req,res) => {
    res.sendFile('./src/index.html')
})

app.use((req, res, next) => {
    res.status(404).sendFile('/404.html')
});


app.listen(4000, () => {
    console.log(`ride on port 4000`);
})