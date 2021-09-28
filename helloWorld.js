function choice(choices) {
  var index = Math.floor(Math.random() * choices.length);
  return choices[index];
}

class parqueadero {
  constructor() {
    this.listaCarros = [0, 2];
    this.listaMotos = [];
  }
  reportarIngresos() {
    var _ingresosParqueaderos =
      this.listaCarros.length * 10000 + this.listaMotos.length * 5000;
    console.log(
      "Las ganancias del parqueadero del primer dia son de: ",
      _ingresosParqueaderos
    );
  }

  generarVehiculos(_numeroVehiculos) {
    for (var i = 0; i < _numeroVehiculos; i++) {
      //            random.seed(1)
      var _tipoVehiculo = choice(["moto", "carro"]);
      if (_tipoVehiculo == "moto") {
        if (this.listaMotos.length < 50) {
          this.listaMotos.push(new vehiculo(_tipoVehiculo));
        }
      }
      if (_tipoVehiculo == "carro") {
        if (this.listaCarros.length < 100) {
          this.listaCarros.push(new vehiculo(_tipoVehiculo));
        }
      }
    }
  }
}

class vehiculo {
  constructor(_tipoVehiculo) {}
}

// comienzo
var parqueaderoEspecial = new parqueadero();
//
parqueaderoEspecial.generarVehiculos(100);
//
parqueaderoEspecial.reportarIngresos();
//
