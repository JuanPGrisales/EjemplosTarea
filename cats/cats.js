// create class catsManager
class catsManager {
  constructor() {
    this.cats = [];
  }
  addCat(feline) {
    this.cats.push(feline);
  }
}
class kitty {
  constructor(catName, age, race) {
    this.catName = catName;
    this.age = age;
    this.race = race;
  }
}

// add cat

let catManager = new catsManager();

let _catName = "antonio";
let _age = 4;
let _race = "siames";

catManager.addCat(new kitty(_catName, _age, _race));
console.log(catManager.cats)
