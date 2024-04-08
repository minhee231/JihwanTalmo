const jihwanTalk_box = document.getElementById('jihwan_talk_box');

document.getElementById('Tukkang').addEventListener('mouseenter', function() {
    jihwanTalk_box.style.display = 'block';
});

document.getElementById('Tukkang').addEventListener('mouseleave', function() {
    jihwanTalk_box.style.display = 'none';
});
