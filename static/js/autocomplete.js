let availableKeywords = [
    'H&M lantai G',
    'Uniqlo',
    'Sociolla',
    'Djournal Coffe Bar',
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
    'Adelle Jewelerry',
    'Timberland',
    'Hyundai',
    'Elevatione',
    'Max Fashion',
    'The Gourmet',
    'Pintu Keluar 9',
    'Lift G',
    'Axel Vinesse',
    'Kopi Kenangan',
    'Pintu Keluar X',
    'Venchi',
    'Loccitane',
    'Eskalator G2',
    'Eskalator G1',
    'Eskalator G3'
];

const resultsBox = document.querySelector(".result-box");
const input1 = document.getElementById("user-data-1");
const input2 = document.getElementById("user-data-2");

document.body.addEventListener("click", function(event) {
    // Check if the clicked element is outside of the resultsBox
    if (!resultsBox.contains(event.target)) {
        resultsBox.innerHTML = ''; // Clear the resultsBox
    }
});


input1.onkeyup = function(){
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
        return "<li onclick = 'selectInput1(this)' class='text-white'>" + list + "</li>";
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
        return "<li onclick = 'selectInput2(this)' class='text-white'>" + list + "</li>";
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