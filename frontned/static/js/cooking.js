export const cook_cookie = {
    token_cook: function(token) {
        document.cookie = `token=${token}`;
    }
}
