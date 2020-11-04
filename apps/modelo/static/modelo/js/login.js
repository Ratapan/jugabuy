// function l()

// fetch('http://127.0.0.1:8000/login', {
//             method: 'POST',
//             body: JSON.stringify({
//                 name: "pepe@gmail.com",
//                 surname: "pepe1234"
//             }),
//             headers: {
//                 "Content-type": "application/json"
//             })
//       .then(response => response.json())
//       .then(json => console.log(json))


var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();

today = mm + '/' + dd + '/' + yyyy;

    function login() {
        
        var $username = document.getElementById("username").value;
        var $password = document.getElementById("password").value
        fetch('http://127.0.0.1:8000/login', {
            method: 'POST', //POST, PUT, DELETE
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers:{'Content-Type': 'application/json',"X-CSRFToken": $crf_token},
            redirect: 'follow',
            body: JSON.stringify(
                {username: $username, 
                 password: $password
                }
                )
        })
            .then(response => response.json())
            .then(data => alert(data.ok)) 

    }

    function register() {
       console.log('23<dszfxgcvb')

        var $us_rut = document.getElementById("rut").value;
        var $us_mail = document.getElementById("Email").value;
        var $us_nom = document.getElementById("Nombre").value;
        var $us_apes = document.getElementById("Apellido").value;
        var $us_contr = document.getElementById("Password4").value;
        var $us_nac = document.getElementById("Date").value;
        //var $us_creac = document.getElementById("").value;
        var $us_tel = document.getElementById("Tel").value;
        var $us_dir = document.getElementById("Address").value
        //var $us_sald = document.getElementById("").value;
        //var $id_rol = document.getElementById("").value;
        //var $id_ciud = document.getElementById("").value;
        

        fetch('http://127.0.0.1:8000/register', {
            method: 'POST', //POST, PUT, DELETE
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers:{'Content-Type': 'application/json',"X-CSRFToken": $crf_token},
            redirect: 'follow',
            body: JSON.stringify(
                {
                 us_rut:parseInt($us_rut),
                 us_mail:$us_mail,
                 us_nom: $us_nom,
                 us_apes:$us_apes,
                 us_contr:$us_contr,
                 us_nac:$us_nac,
                 us_creac:today,
                 us_tel:parseInt($us_tel),
                 us_dir:$us_dir,
                 us_sald:0,
                 id_rol:1,
                 id_ciud:1
                
                }
                )
        })
            .then(response => response.json())
            .then(data => alert(data.ok)) 

    }