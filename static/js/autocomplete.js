let availableKeywords = [

    //lantai 0
    'H&M Lantai G',
    'Sociolla',
    'Djournal Coffee Bar',
    'Starbucks Reserve',
    'Marks & Spencer',
    'Pandora',
    'Frank&Co',
    'Tumi',
    'Pintu Keluar 10',
    'Elemis',
    'Miss Mondial',
    "Ling's Sister Jewellery",
    'Melissa Clube',
    'Adelle Jewellery',
    'Timberland',
    'Hyundai',
    'Elevatione',
    'Max Fashion',
    'The Gourmet',
    'Pintu Keluar 9',
    'Axel Vinesse',
    'Kopi Kenangan',
    'Pintu Keluar X', //lupa pintu keluar brp
    'Venchi',
    'Loccitane',
    'Marquine',

    //lantai 1

    'Uniqlo',
    'Amarissa',
    'Bridges Optical',
    'Cheskee',
    'Colorbox',
    'The Executive',
    'KKV Lantai 1',
    'LockNLock',
    'Miniso',
    'Carla',
    'Parkiran', //lupa parkiran yang mana
    'Urban & Co',
    'Koi The',
    'Dr. Specs',
    'Stop N Go',
    "Levi's",
    'Watch Club',
    'Polo',
    'Glam On',
    'Fossil',
    'Optik Seis Signature',
    'Owl Optical',
    'Zeiss Vision Center',
    'H&M Lantai 1',

    //lantai 2
    "Home & Living",
    "Malinda Furniture Gallery",
    "Vivere",
    "Idemu",
    "Payless Shoes",
    "Padre",
    "Iuiga",
    "Urban Republic",
    "Vans",
    "Asics",
    "The Athlete's Foot",
    'Puma',
    'New Era',
    'The North Face',
    'Hoops',
    'Seek',
    'KKV Lantai 2',
    'Lao Fook',
    'Pan & Co',
    'Planet Sports Asia',
    'Converse',
    'Crocs',
    "Tucano's",
    'Adidas',
    'Wee Nam Kee',
    'Fila',

    //lantai 3
    'Jiggle Jungle',
    'Reformed Exodus Community',
    'Magal Korean BBQ',
    'Saga Japanese Restaurant',
    'LinCafe',
    'BonCafe',
    'Natural Farm',
    'Shinjuku',
    'Mi Store',
    'Guardian Plus',
    'Vlife Medical',
    'Huawei',
    'Oppo',
    'House of David',
    'Scoop Ideas',
    'Maison Feerie',
    'Pure Clinic',
    'Puro Clinic',
    'Justice',
    'Samsung',
    'Willio',
    'GingerSnaps',
    'Mothercare',
    'Watsons GM3',
    'Nona Manis',

    //lantai 4
    'Timezone GM3',
    'ATM BCA GM3',
    'Bakmi GM',
    'Fusia',
    'Ichiban Sushi',
    'Steak 21',
    'Food Court',
    'Poke Theory',
    'Burger King',
    'Crunchaus',
    'Jack & John',
    'Shaburi & Kintan',
    'International Christian Assembly'


];

const resultsBox = document.querySelector(".result-box");
const pathBox = document.querySelector(".path-box");
const choiceBox = document.querySelector(".choice-box");
const ket = document.querySelector(".keterangan");
const input1 = document.getElementById("user-data-1");
const input2 = document.getElementById("user-data-2");

document.body.addEventListener("click", function(event) {
    // Check if the clicked element is outside of the resultsBox
    if (!resultsBox.contains(event.target)) {
        resultsBox.innerHTML = ''; // Clear the resultsBox
    }
});


input1.onkeyup = function(){
    pathBox.innerHTML = '';
    choiceBox.innerHTML = '';
    ket.innerHTML = '';

    let result = [];
    let input = input1.value;
    if (input.length){
        result = availableKeywords.filter((keyword) => {
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log(result);
    }
    display1(result);

    if (!result.length){
        resultsBox.innerHTML = '';
    }
}

function display1(result){
    const content = result.map((list) => {
        return "<li onclick = 'selectInput1(this)' class=''>" + list + "</li>";
    });

    resultsBox.innerHTML = "<ul>" + content.join('') + "</ul>";
}

function selectInput1(list){
    const parser = new DOMParser();
    const decodedText = parser.parseFromString(list.innerHTML, 'text/html').body.textContent;
    console.log(decodedText);

    input1.value = decodedText;
    resultsBox.innerHTML = '';
}

input2.onkeyup = function(){
    pathBox.innerHTML = '';
    choiceBox.innerHTML = '';
    ket.innerHTML = '';

    let result = [];
    let input = input2.value;
    if (input.length){
        result = availableKeywords.filter((keyword) => {
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log(result);
    }
    display2(result);

    if (!result.length){
        resultsBox.innerHTML = '';
    }
}

function display2(result){
    const content = result.map((list) => {
        return "<li onclick = 'selectInput2(this)' class=''>" + list + "</li>";
    });

    resultsBox.innerHTML = "<ul>" + content.join('') + "</ul>";
}

function selectInput2(list){
    const parser = new DOMParser();
    const decodedText = parser.parseFromString(list.innerHTML, 'text/html').body.textContent;
    console.log(decodedText);

    input2.value = decodedText;
    resultsBox.innerHTML = '';
}

resultsBox.addEventListener("click", function(event) {
    event.stopPropagation();
});