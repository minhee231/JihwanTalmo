const jihwan_hair1 = document.getElementById("jihwan_hair1");
const jihwan_hair2 = document.getElementById("jihwan_hair2");
const jihwan_hair3 = document.getElementById("jihwan_hair3");
const jihwan_hair4 = document.getElementById("jihwan_hair4");
const jihwan_hair5 = document.getElementById("jihwan_hair5");

const harvest_button = document.getElementById("harvest_button");

const hair_element_list = [
    jihwan_hair1,
    jihwan_hair2,
    jihwan_hair3,
    jihwan_hair4,
    jihwan_hair5,
];

const hair_move_class = [
    'up_hair_type1',
    'up_hair_type2',
    'up_hair_type3',
];

function clearHairMoveClasses(elements) {
    elements.forEach(hair => {
        hair_move_class.forEach(className => {
            hair.classList.remove(className);
        });
    });
}

function move_jihwan_hair(elements, count) {
    clearHairMoveClasses(elements)
    elements.forEach(hair => {
        const random_index = Math.floor(Math.random() * hair_move_class.length);
        const random_move_class = hair_move_class[random_index];

        hair.classList.add(random_move_class);
    });
};

let hair_element_count = 0;
harvest_button.addEventListener('click', () => move_jihwan_hair(hair_element_list));


