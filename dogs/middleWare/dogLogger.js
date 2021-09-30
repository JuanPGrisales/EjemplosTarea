class dogLogger {
  constructor() {
    this.dogs = []; // = leer de base de datos dogs
  }
  saveNewDog(name, race, age) {
    this.dogs.push(new dog(name, race, age)); // push a la base de datos
  }
  getDogs() {
    return this.dogs; // leer de la base de datos
  }
}

class dog {
  constructor(name, race, age) {
    this.name = name;
    this.race = race;
    this.age = age;
  }
}

let myDogLogger = new dogLogger();

module.exports = myDogLogger;
