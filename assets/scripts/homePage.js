
window.addEventListener('load', () => {
    document.getElementById('message').textContent = 'rr!';
}); 


var comps = document.querySelectorAll(".product>div")

for(let comp in comps)
{
    let id = comps[comp].querySelector("input").value
    let title = comps[comp].querySelector(".productTitle").textContent.replace(" ", "-")
    // comps[comp].onclick = function(e){
    //     window.location =`products/${id}/${title}`;
    // }; keyup

    comps[comp].addEventListener("mousedown", function(e){
        e.stopPropagation()
        if(e.button == 0){

            if(e.ctrlKey){
                window.open(`products/${id}/${title}`,'_blank');
            }
            else
            {
                window.location =`products/${id}/${title}`;
            }
        }
        else if(e.button == 1){
            window.open(`products/${id}/${title}`,'_blank');
        }
        // console.log(e.button)
    })

    // if (event.ctrlKey) {
    //     text = "The CTRL key was pressed!";
    //   } else {
    //     text = "The CTRL key was NOT pressed!";
    // }

    //   comps[comp].onauxclick = (e) => {
    //     e.preventDefault();
    //     console.log("e.button")
    // };
}