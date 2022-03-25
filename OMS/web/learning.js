function displayDate(){
    var txt = "Today is " + Date();
    document.getElementById('fname').value = txt;
}

function clearDate(){
    document.getElementById('fname').value = "";
}

function getInventory(){
    var value = "";//TODO:  Make an http call to get the value

    axios.get("http://127.0.0.1:5000/inventory/list")
    .then((response) => {
        console.log(response.data)
        value = response.data.toString();
        document.getElementById('fname').innerHTML= value;
     }, (error) => {
        console.log(error);
     });

}