import { serverConfig } from '../../config.js';
//const { serverConfig } = require('../../config.js');

function get_talmo_title() {

    fetch(`${serverConfig.apiUrl}/get/talmo-title`)
    // fetch('http://localhost:5000/get/talmo-title')
    .then(response => response.text())

    .then(text => {
        document.getElementById('talmo_title').textContent = text;
    })

    .catch(error => console.error('Error:', error));
};

function get_talmo_him() {
    fetch(`${serverConfig.apiUrl}/get/talmo-him`)
    .then(response => response.text())

    .then(text => {
        document.getElementById('talmo_him_do').textContent = text;
    })

    .catch(error => console.error('Error:', error));
};

function add_talmo_him() {
    fetch(`${serverConfig.apiUrl}/add/talmo-him`)
    .then(response => response.text())

    .catch(error => console.error('Error:', error));
};

//document.getElementById('add_talmo').addEventListener('click', add_talmo_him);
document.getElementById('add_talmo').addEventListener('click', function () {
    add_talmo_him()
    get_talmo_him()
});

//로딩이 완료되면 실행 ======================================================
document.addEventListener('DOMContentLoaded', function() {
    get_talmo_title();
    get_talmo_him();
});