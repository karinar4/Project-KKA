let availableKeywords = [
    'H&M',
    'Uniqlo'
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