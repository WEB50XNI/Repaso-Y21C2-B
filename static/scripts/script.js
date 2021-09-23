document.addEventListener('DOMContentLoaded', function(){
    console.log("Cargado :D");
    window.onpopstate = e =>{
        const data = e.state;
        document.title=data.title;
        document.getElementById("contenidoDinamico").innerHTML=data.text;

    };
});

function renderHTML(ruta){
    let request = new XMLHttpRequest();
    request.open('GET', ruta);

    request.onload = function(){
        if(request.status == 200){
            let res=request.responseText;
            let content= document.getElementById("contenidoDinamico");
            content.innerHTML=res;
            history.pushState(document.textContent, ruta, ruta)
            return false;
        }
        else{
            alert("Ups.. Algo salió mal, no te preocupes, no es culpa tuya.")
            return false;
        }
    };
    request.send();
}

function agregar(form){
    let data = new FormData(form);
    let request= new XMLHttpRequest();
    request.open("POST", "/agregar");
    request.onload = function(){
        if(request.status == 200){
            document.querySelectorAll("input").forEach(input)= function(){
                input.text="";
            };
            alert("Agregado con exito")
            let res=request.responseText;
            let content= document.getElementById("contenidoDinamico");
            content.innerHTML=res;
            history.pushState(document.textContent, ruta, ruta)
            return false;
        }
        else{
            alert("Ups.. Algo salió mal, no te preocupes, no es culpa tuya.")
            return false;
        }

    };
    request.send(data);
}