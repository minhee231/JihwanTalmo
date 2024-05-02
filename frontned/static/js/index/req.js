import { serverConfig } from '../config.js';

function get_talmo_title() {

    fetch(serverConfig.index_page.get.talmo_gione_title)
    .then(response => response.text())

    .then(text => {
        document.getElementById('talmo_title').textContent = text;
    })

    .catch(error => console.error('Error:', error));
};

function get_talmo_him() {
    fetch(serverConfig.index_page.get.talmo_him)
    .then(response => response.text())

    .then(text => {
        document.getElementById('talmo_him_do').textContent = text;
    })

    .catch(error => console.error('Error:', error));
};

function add_talmo_him() {
    fetch(serverConfig.index_page.add.talmo_him)
    .then(response => response.text())

    .catch(error => console.error('Error:', error));
};

function redirect_login_url() {
    fetch(serverConfig.get.login_url)
    .then(response => response.text())

    .then(text => {
        window.location.href = text;
    })

    .catch(error => console.error('Error:', error));
};

document.getElementById('add_talmo').addEventListener('click', function () {
    add_talmo_him()
    get_talmo_him()
});

document.getElementById('go_mari').addEventListener('click', redirect_login_url)

get_talmo_title();
get_talmo_him();


