// const web = "https://jihwan-talmo.x-coll.com"
// const login_api = "https://login.jihwan-talmo.x-coll.com"
// const index_page_api = "https://indexp.jihwan-talmo.x-coll.com"
// const user_api = "https://user.jihwan-talmo.x-coll.com"

const web = "http://localhost:3400" //개발전용
const login_api = "http://43.203.18.191:429" //요금 절감
const index_page_api = "http://43.203.18.191:687" //요금 절감
const user_api = "http://43.203.18.191:538" //요금 절감

export const serverConfig = {
    server_url: {
        web: web,
        login_api: login_api,
        index_page_api: index_page_api,
        user_api: user_api,
    },

    index_page: {
        add: {
            talmo_him: `${index_page_api}/add/talmo-him`
        },

        get: {
            talmo_gione_title: `${index_page_api}/get/talmo-title`,
            talmo_him: `${index_page_api}/get/talmo-him`,
            login_url: `${login_api}/get/login_url`,
        },
    },

    login_page: {
        get: {
            access_token : `${login_api}/get/access-token`,
            user_info : `${login_api}/get/user-info` //test
        },
    },

    user: {
        get: {
            user_info: `${user_api}/get/user-info`,
        },

        add: {
            owned_hair: `${user_api}/add/hair`,
        }
    },

}