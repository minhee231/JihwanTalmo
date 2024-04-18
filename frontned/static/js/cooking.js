export const cook_cookie = {
    token_cook: function(token) {
        document.cookie = `token=${token}`;
    },

    load_cookie : function(cookie_name) {
    
        const cookieArray = document.cookie.split(';');
        
        for (let i = 0; i < cookieArray.length; i++) {
            let cookie = cookieArray[i];

            while (cookie.charAt(0) === ' ') {
                cookie = cookie.substring(1);
            }

            if (cookie.indexOf(cookie_name + '=') === 0) {
                return cookie.substring(cookie_name.length + 1, cookie.length);
            }
        }
        console.log("not found cookie")
        return null;
    }
}