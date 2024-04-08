import { serverConfig } from '../config.js';
import { cook_cookie } from './cooking.js'

function get_user_info() {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');

    fetch(`${serverConfig.login.request_login_api}?code=${code}`)
    .then(response => response.json())

    .then(data => console.log(data))

    .catch(error => console.error('Error:', error));
}

function get_access_token() {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');

    fetch(`${serverConfig.get.access_token}?code=${code}`)
    .then(response => response.text())

    .then(text => {
        cook_cookie.token_cook(text);
        return text})

    .catch(error => console.error('Error:', error));
}