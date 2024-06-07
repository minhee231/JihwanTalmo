const change_bg_button = document.getElementById("change_bg_button");
const background_element = document.getElementsByTagName("body")[0];
let bg_status = false

//false == 지환쌤 On
function change_bg() {
    if (bg_status) {
        background_element.style.backgroundImage = "none";
        bg_status = false;
    }
    else if (!bg_status) {
        background_element.style.backgroundImage = "url(/static/images/index/SingingJiHwanT.gif";
        bg_status = true;
    }
}
console.log("불러오기 성공")

change_bg_button.addEventListener('click', function(){
    change_bg();
});