//Code adapted from: https://pythonise.com/categories/javascript/infinite-lazy-loading#the-javascript

var scroller = document.querySelector('#scroller');
var post = document.querySelector('#post');
var sentinel = document.querySelector('#sentinel');
var template = document.querySelector('#post_template');

var counter = 0;



//requests new posts
function loadItems() {

    //fetches posts w/ counter
    fetch(`/load?c=${counter}`).then((response) => {
        //converst to json
        response.json().then((data) => {
            sentinel.innerHTML = "Loading...";
            if (counter == 0 && !data.length){
                document.getElementById("about-post-backup").style.visibility = "visible";
                sentinel.innerHTML = "No posts found";
                return;
            }
            // if no more posts/empty json, exit the function
            if (!data.length) {
                // place no more posts text
                sentinel.innerHTML = "No more posts";
                return;
            }
            console.log(data)
            
            //console.log(data[0])
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
                document.getElementById("about-post-backup").style.visibility = "hidden";
                counter += 1;
            }
        })
    })
}
// Create a new IntersectionObserver instance
var intersectionObserver = new IntersectionObserver(entries => {

    // Uncomment below to see the entry.intersectionRatio when
    // the sentinel comes into view
  
    /*entries.forEach(entry => {
       console.log(entry.intersectionRatio);
    })*/
  
    // If intersectionRatio is 0, the sentinel is out of view
    // and we don't need to do anything. Exit the function
    if (entries[0].intersectionRatio <= 0) {
      return;
    }
    // Call the loadItems function
    loadItems();  
  });
  // Instruct the IntersectionObserver to watch the sentinel
intersectionObserver.observe(sentinel);
