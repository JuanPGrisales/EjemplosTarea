let express = require("express");
let myDogLogger = require("../middleWare/dogLogger.js")
let router = express.Router();

router.get("/", (req, res) => {
  res.send(myDogLogger.getDogs());
});

module.exports = router;
