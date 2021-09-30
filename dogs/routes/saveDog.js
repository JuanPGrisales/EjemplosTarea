let express = require("express");
let myDogLogger = require("../middleWare/dogLogger.js")
let router = express.Router();

router.post("/", (req, res) => {
  let name = req.body.name;
  let race = req.body.race;
  let age = req.body.age;

  myDogLogger.saveNewDog(name, race, age);
  res.send("success!");
});

module.exports = router;
