function autocompleteMail() // check changes manually made in information box (right box)
{
    document.getElementById("mailInput").value = document.getElementById("nameInput").value.toLowerCase() +"."+ document.getElementById("lastNameInput").value.toLowerCase()  + "@pwr.edu.pl";
}