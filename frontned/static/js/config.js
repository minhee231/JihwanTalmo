//const api_url = "https://api.x-coll.com"
const api_url = "http://localhost:5000"; //개발할 때 사용
//const web_url = "https://jihwan-talmo.x-coll.com"
const web_url = "http://localhost:3400"

export const serverConfig = {
    server_url: {
        web: web_url,
        api: api_url,
    },

    add: {
        talmo_him: `${api_url}/add/talmo-him`,
    },
    
    get: {
        talmo_gione_title: `${api_url}/get/talmo-title`,
        talmo_him: `${api_url}/get/talmo-him`,

        login_url : `${api_url}/get/login_url`,
        access_token: `${api_url}/get/access-token`
        
    },

    login: {
        request_login_api: `${api_url}/login-callback`
    }

}