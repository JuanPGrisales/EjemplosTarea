class dogLogger {

    constructor (){
        this.dogs = []
    }
    saveDog(doge) {
    this.dogs.push(doge)
    }
}

class dog {
 constructor (name, race, age) {
     this.name = name
     this.race = race
     this.age = age
 }
}

const express = require('express')
const app = express()
const port = 3000

const cors = require('cors');
app.use(cors({
    origin: '*'
}));

var jsonParser = require('body-parser').json()

let myDogLogger = new dogLogger();

app.get('/', (req, res) => {
  res.send('Backend DogLogger')
})

app.post('/saveDog', jsonParser, (req, res) => {

    let name = req.body.name
    let race = req.body.race
    let age = req.body.age

    myDogLogger.saveDog(new dog(name, race, age))
    res.send("success!")
})

app.get('/dogs', (req, res) => {
    res.send(myDogLogger.dogs)
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})


