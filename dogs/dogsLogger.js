$(document).ready(function () {
  refreshDogTable();

  $("#buttonADD").click(function () {
    $("#dogLogger").css("display", "none");
    $("#addNewLogger").css("display", "flex");
  });

  $("#buttonAddNew").click(function () {
    let nameDog = $("#nameInput").val();
    let raceDog = $("#raceInput").val();
    let ageDog = $("#ageInput").val();

    let dog = {
      name: nameDog,
      race: raceDog,
      age: ageDog,
    };

    var http = new XMLHttpRequest();
    var url = "http://localhost:3000/saveDog";
    http.open("POST", url, true);
    //Send the proper header information along with the request
    http.setRequestHeader("Content-type", "application/json");

    http.onreadystatechange = function () {
      if (http.readyState === 4 && http.status === 200) {
        $("#addNewLogger").css("display", "none");
        $("#dogLogger").css("display", "flex");
        refreshDogTable();
      }
    };

    http.send(JSON.stringify(dog));
  });

  function refreshDogTable() {
    var http = new XMLHttpRequest();
    http.open("GET", "http://localhost:3000/dogs", false); // false for synchronous request
    http.send(null);
    let dogs = JSON.parse(http.responseText);

    $("tbody").empty();
    dogs.forEach((dog) => {
      markup = `
      <tr>
        <td>
          ${dog.name}
        </td>
        <td>
          ${dog.race}
        </td>
        <td>
          ${dog.age}
        </td>
      </tr>`;
      $("#tableInfo tbody").append(markup);
    });
  }
});
