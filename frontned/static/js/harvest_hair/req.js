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

// function get_user_info() {
//     const token = cook_cookie.load_cookie("token");
//     const encodedToken = encodeURIComponent(token);

//     fetch(`${serverConfig.login_page.get.user_info}?access_token=${encodedToken}`)
//     .then(response => response.json())

//     .then(data => console.log(data))

//     .catch(error => console.error('Error:', error));
// }

function get_user_info() {
    const token = cook_cookie.load_cookie("token");
    const encodedToken = encodeURIComponent(token);

    fetch(`${serverConfig.user.get.user_info}?access_token=${encodedToken}`)
    .then(response => response.json())

    .then(data => {
        document.getElementById('sujip_hair_amount').textContent = "수집된 머리카락의 수 : " + data.harvest_hair_page.owned_hair_count;
    })

    .catch(error => console.error('Error:', error));
}


get_user_info();