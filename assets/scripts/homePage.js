
// window.addEventListener('load', () => {
//     document.getElementById('message').textContent = 'rr!';
// }); 

let comps = document.querySelectorAll(".product>div")

comps.forEach(comp => {
    // console.log(comp)
    let id = comp.querySelector("input").value
    let title = comp.querySelector(".productTitle").textContent.replace(" ", "-")

    
    comp.addEventListener("mousedown", function(e){
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
    })

});
