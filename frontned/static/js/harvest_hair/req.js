import { serverConfig } from '../config.js';
import { cook_cookie } from '../cooking.js'

function get_user_info() {
    const token = cook_cookie.load_cookie("token");
    const encodedToken = encodeURIComponent(token);

    fetch(`${serverConfig.user.get.user_info}?access_token=${encodedToken}`)
    .then(response => response.json())

    .then(data => {
        document.getElementById('sujip_hair_amount').textContent = "수집된 머리카락의 수 : " + data.harvest_hair_page.owned_hair_count;

        console.log(data);
    })

    .catch(error => console.error('Error:', error));
}

function add_hair() {
    const token = cook_cookie.load_cookie("token");
    const encodedToken = encodeURIComponent(token);

    fetch(`${serverConfig.user.add.owned_hair}?access_token=${encodedToken}`)
    .then(response => response.text())

    .then(text => {
        document.getElementById('sujip_hair_amount').textContent = "수집된 머리카락의 수 : " + text;
    })

    .catch(error => console.error('Error:', error));
}

document.getElementById('harvest_button').addEventListener('click', function () {
    add_hair();
});

get_user_info();