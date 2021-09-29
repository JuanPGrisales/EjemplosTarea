// create class catsManager
class catsManager {
  constructor() {
    this.cats = [];
  }
  addNewCat(name, age, race) {
    this.cats.push(new kitty(name, age, race));
  }
}
class kitty {
  constructor(catName, age, race) {
    this.catName = catName;
    this.age = age;
    this.race = race;
  }
}

let catManager = new catsManager();

const express = require('express');
const app = express();
const port = 3000;

app.use(require('body-parser').json())

const cors = require('cors');
app.use(
  cors({
    origin: '*'
  })
);

let cat = new catsManager();

app.get('/', (req, res) => {
  res.send('home');
});

app.post('/addNewCat', (req, res) => {
  let catName = req.body.x
  let age = req.body.y
  let race = req.body.z
  catManager.addNewCat(catName, age, race);
  res.send(true);
});

app.get('/cats', (req, res) => {
  res.send(JSON.stringify(catManager.cats));
});

















app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});
