//Code adapted from: https://pythonise.com/categories/javascript/infinite-lazy-loading#the-javascript

var template = document.querySelector('#post_template');
var sentinel = document.querySelector('#sentinel');

lists = document.getElementsByClassName("post-text")
var results = [];
for (i = 0; i < lists.length; i++) {
    var contents = lists[i].innerHTML;
    console.log(contents)
    var texts = contents.split("&gt;");
    texts = texts.join(">");
    results[i] = texts;
    texts = results[i].split("&lt;");
    texts = texts.join("<");
    results[i] = texts;
    console.log(results)
}


text = document.getElementById("post-text")
var textB = text.parentNode;
textB.removeChild(text);
textB.innerHTML = textB.innerHTML + results;

//loadItems();
/*
function loadItems() {

    //fetches all posts
    fetch(`/projectload?c=all`).then((response) => {
        //converst to json
        response.json().then((data) => {
            if (!data.length){
                sentinel.innerHTML = "No projects found";
                return;
            }
            for (var i = 0; i < data.length; i++) {
                let template_clone = template.content.cloneNode(true);
                var tempA = document.createElement('a');
                tempA.href = `${data[i].url}`;
                var linkText = document.createTextNode(`${data[i].title}:`);
                tempA.append(linkText);

                template_clone.querySelector("#title").insertAdjacentElement('afterbegin',tempA);
                //template_clone.querySelector("#title").innerHTML = ` `;
                template_clone.querySelector("#post").innerHTML = `${data[i].blurb}`;
                scroller.appendChild(template_clone);
            }
        })
    })
}*/