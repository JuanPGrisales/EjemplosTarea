$(document).ready(function () {
  let myDogLogger = new dogLogger();
  refreshDogTable();

  $("#buttonADD").click(function () {
    $("#dogLogger").css("display", "none");
    $("#addNewLogger").css("display", "flex");
  });

  $("#buttonAddNew").click(function () {
    let nameDog = $("#nameInput").val();
    let raceDog = $("#raceInput").val();
    let ageDog = $("#ageInput").val();
    myDogLogger.saveDog(new dog(nameDog, raceDog, ageDog));
    $("#addNewLogger").css("display", "none");
    $("#dogLogger").css("display", "flex");
    refreshDogTable();
  });

  function refreshDogTable() {
    let dogs = myDogLogger.dogs;
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
