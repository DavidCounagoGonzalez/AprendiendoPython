const listarComunicados = async (busqueda, estado, tipo) => {
    try {
        const response = await fetch('/gestion/listar/'); //Recibe los datos en forma de json registrados en esa url
        const data = await response.json(); //Transforma el json en un objeto de js
        if (data.message === "Success") { //Comprobamos que se haya producido la transacción
            let lista = "";
            data.comunicados.forEach((comunicado) => { //Recorremos los datos recibidos aplicando los filtros solicitados
                if (comunicado.token.includes(busqueda)) { //Aquellos que el token contenga con lo indicado en el input
                    if(comunicado.tipo_id.includes(tipo)){ //Aquellos que sean del mismo tipo indicado en el select
                    if (estado) { //EN este if recogerá también los solucionados y en caso de estar solucionados también se mostrarán con fondo verde
                        lista += `<tr class="table ${comunicado.solucionado ? 'table-success' : ''}"> 
                    <td>${comunicado.token}</td>
                    <td>${comunicado.tipo_id}</td>
                    <td>${comunicado.comunicante_id}</td>
                    <td>${comunicado.fecha}</td>
                    <td><a href="${comunicado.token}" class="btn btn-default ml-1"><i class="fa-regular fa-eye"></i></a></td>
                </tr>`
                    } else if(comunicado.solucionado === false) {
                        lista += `<tr class="table ${comunicado.solucionado ? 'table-success' : ''}">
                    <td>${comunicado.token}</td>
                    <td>${comunicado.tipo_id}</td>
                    <td>${comunicado.comunicante_id}</td>
                    <td>${comunicado.fecha}</td>
                    <td><a href="${comunicado.token}" class="btn btn-default ml-1"><i class="fa-regular fa-eye"></i></a></td>
                    </tr>`
                        
                    }
                }
                }
            });
            cuerpoTabla.innerHTML = lista; //Añadimos la lista de filas guardadas posteriormente al cuerpod e la tabla en el html
        } else {
            alert("Comunicados no encontrados...")
        }
    } catch (error) {
        console.log(error);
    }
}

const cargaInicial = async () => {
    await listarComunicados('', true, ''); //Carga de inicio la función sin filtros
    
    //Los eventos se lanzan cada vez que se detecta un cambio en los inputs recogiendo los datos/estado del los demás paar cargar todos los filtros

    buscar.addEventListener("input", (event) => { //Lanza la función cada vez que se detecta un añadido en el input text
        if (solucionado.checked) {
            estado = true;
        } else {
            estado = false;
        }

        if (id_tipo.value === ''){
            tipo = ''
        }else{
            tipo = id_tipo.options[id_tipo.selectedIndex].text
        } 

        listarComunicados(event.target.value, estado, tipo) 
    })

    solucionado.addEventListener("change", (event) => { //Cada vez que cambia el estado del checkbox
        if (event.target.checked) {
            estado = true;
        } else {
            estado = false;
        }

        if (id_tipo.value === ''){
            tipo = ''
        }else{
            tipo = id_tipo.options[id_tipo.selectedIndex].text
        }  

        listarComunicados(buscar.value, estado, tipo)
    })

    id_tipo.addEventListener("change", (event) => {
        if (solucionado.checked) {
            estado = true;
        } else {
            estado = false;
        }

        if (event.target.value === ''){
            tipo = ''
        }else{
            tipo = event.target.options[event.target.selectedIndex].text
        }  

        listarComunicados(buscar.value, estado, tipo)
    })
};

window.addEventListener("load", async () => {
    await cargaInicial();
})