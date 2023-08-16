const express = require('express');
const fs = require('fs/promises');
const app = express();

app.set('view engine', 'ejs');

app.use('/static', express.static('static'));

app.get('/', (req, res) => {
    res.sendFile(`${__dirname}/index.html`);
});

app.get('/robots.txt', (req, res) => {
    res.type("text/plain");
    res.send(`User-agent: *\nAllow: /\n`);
});

app.get('/detail/:year/:month/:day', async (req, res) => {
    const { year, month, day } = req.params;
    const filename = `KBO${year}-${month}-${day}.png`;
    const filePath = `${__dirname}/static/${filename}`;

    try {
        await fs.access(filePath);
        res.render("detail", { year, month, day });
    } catch (err) {
        res.sendFile(`${__dirname}/404.html`);
    }
});

app.use((req, res, next) => {
    res.status(404).sendFile(`${__dirname}/404.html`);
});

app.listen(4000, () => {
    console.log(`🏄 ride on port 4000`);
});
