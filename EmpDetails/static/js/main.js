$(document).ready(function(){

      $("#submit").click(function(){
        clearValues();
        empId = document.getElementById("employeeId").value;
        $.ajax({
            type: 'GET',
            url: "http://localhost:5000/getEmployeeDetails?employeeId="+empId,
            success:function(data){
              //alert(data.firstName);
              setValues(data);
            },
           error: function(xhr, status, text) {
              alert(xhr.responseText);
           }
        });
  });
});


function clearValues(){
  elems = document.getElementsByClassName("value");
  for (const x of elems) { x.innerHTML = ""; }
}

function setValues(data){
  document.getElementById("fname").innerHTML = data.firstName;
  document.getElementById("lname").innerHTML = data.lastName;
  document.getElementById("phoneNo").innerHTML = data.phoneNo;
  document.getElementById("city").innerHTML = data.city;
}
