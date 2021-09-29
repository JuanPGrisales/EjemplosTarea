$(document).ready(function () {
  
    tableRefresh();

  function tableRefresh() {
    Http = new XMLHttpRequest();
    url = "http://localhost:3000/cats";
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
      if (Http.readyState == 4 && Http.status == 200) {
        let cats = JSON.parse(Http.responseText);

        $("tbody").empty();
        cats.forEach((cat) => {
          markup = `
          <tr>
            <td>
              ${cat.catName}
            </td>
            <td>
              ${cat.age}
            </td>
            <td>
              ${cat.race}
            </td>
          </tr>`;
          $("#tableInfo tbody").append(markup);
        });
      }
    };
  }

  $("#buttonAddNew").click(function () {
    $("#catManager").css("display", "none");
    $("#catAdder").css("display", "flex");
  });

  $("#buttonAddCat").click(function () {
    let catName = $("#inputName").val();
    let age = $("#inputAge").val();
    let race = $("#inputRace").val();

    let Http = new XMLHttpRequest();
    let url = "http://localhost:3000/addNewCat";
    Http.open("POST", url);
    let newObj = {
      x: catName,
      y: age,
      z: race,
    };

    Http.setRequestHeader("Content-type", "application/json");
    Http.send(JSON.stringify(newObj));

    Http.onreadystatechange = (e) => {
      if (Http.readyState == 4 && Http.status == 200) {
        $("#catAdder").css("display", "none");
        $("#catManager").css("display", "flex");
        tableRefresh();
      }
    };
  });
});
