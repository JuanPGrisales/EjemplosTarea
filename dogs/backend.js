let dogsRouter = require("./routes/dogs.js")
let indexRouter = require("./routes/index.js")
let saveDogRouter = require("./routes/saveDog.js")


const express = require('express')
const app = express()
const port = 3000

const cors = require('cors');
app.use(cors({
    origin: '*'
}));

app.use(require('body-parser').json())


app.use('/', indexRouter)

app.use('/saveNewDog', saveDogRouter)

app.use('/dogs', dogsRouter)

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})


