let config = {
    frontend : {
        dominio: "http://localhost:5500/"
    },
    backend : {
        dominio: "http://localhost:3000/",
        routes: {
            dogs : "http://localhost:3000/dogs/",
            saveDog: "http://localhost:3000/saveNewDog/"
        }
    }
}

module.exports = config