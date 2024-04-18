import { serverConfig } from '../config.js';
import { cook_cookie } from '../cooking.js'

// function get_user_info() {
//     const urlParams = new URLSearchParams(window.location.search);
//     const code = urlParams.get('code');

//     fetch(`${serverConfig.login.request_login_api}?code=${code}`)
//     .then(response => response.json())

//     .then(data => console.log(data))

//     .catch(error => console.error('Error:', error));
// }

function login_check() {
    const token = cook_cookie.load_cookie("token");
    const encodedToken = encodeURIComponent(token);

    return fetch(`${serverConfig.check.login_check}?access_token=${encodedToken}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            return data;
        })

        .catch(error => {
            console.error('Error:', error)
            throw error;
        });
}

function get_user_info() {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');

    fetch(`${serverConfig.login.request_login_api}?code=${code}`)
    .then(response => response.json())

    .then(data => console.log(data))

    .catch(error => console.error('Error:', error));
}