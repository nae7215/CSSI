console.log("Hello world!");

$(document).ready(
  function() {

    $("#insert_button").click(createListElement /*creating a function is too confusing; define below and call here*/);
  }
)

function createListElement() {
  var person = $("#assignee").val();
  var task = $("#new_task").val();
  $("#tasklist").append("<li>" + person + " " + task + "</li>")
}
