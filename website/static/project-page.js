//Code adapted from: https://pythonise.com/categories/javascript/infinite-lazy-loading#the-javascript

var template = document.querySelector('#post_template');
var sentinel = document.querySelector('#sentinel');

var title = document.getElementById('title');

var contents = title.innerHTML;
contents = contents.split(" ")
contents = contents.join("")
console.log(contents)



loadItems();

function loadItems() {
    //fetches all posts
    
    fetch(`/postload?c=`+contents).then((response) => {
        //converst to json
        response.json().then((data) => {
            if (!data.length){
                sentinel.innerHTML = "No posts found";
                return;
            }
            
            for (var i = 0; i < data.length; i++) {
                let template_clone = template.content.cloneNode(true);
                var tempA = document.createElement('a');
                tempA.href = `${data[i].url}`;
                var linkText = document.createTextNode(`${data[i].title}`);
                tempA.append(linkText);

                template_clone.querySelector("#title").insertAdjacentElement('afterbegin',tempA);
                //template_clone.querySelector("#title").innerHTML = ` `;
                template_clone.querySelector("#post").innerHTML = `${data[i].blurb}`;
                scroller.appendChild(template_clone);
            }
        })
    })
}