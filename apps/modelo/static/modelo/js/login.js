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


    function login() {
        var $username = document.getElementById("username").value;
        var $password = document.getElementById("password").value
        console.log($username)
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