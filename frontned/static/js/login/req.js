import { serverConfig } from '../config.js';
import { cook_cookie } from '../cooking.js'

function get_user_info() {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');

    fetch(`${serverConfig.login.request_login_api}?code=${code}`)
    .then(response => response.json())

    .then(data => console.log(data))

    .catch(error => console.error('Error:', error));
}

function redirect_to_harvest() {
    const redirect_path = `${serverConfig.server_url.web}/harvest-hair`
    window.location.href = redirect_path;
};

function get_access_token() {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');

    return fetch(`${serverConfig.get.access_token}?code=${code}`)
        .then(response => response.text())
        .then(text => {
            return text;
        })
        .catch(error => {
            console.error('Error:', error);
            throw error;
        });
}

get_access_token().then(token => {
    cook_cookie.token_cook(token);
    redirect_to_harvest();
}).catch(error => {
    console.error('Error in token processing:', error);
});
