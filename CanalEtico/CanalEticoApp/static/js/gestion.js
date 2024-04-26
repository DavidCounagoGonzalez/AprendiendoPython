const listarComunicados = async (busqueda, estado, tipo) => {
    try {
        const response = await fetch('/gestion/listar/');
        const data = await response.json();
        if (data.message === "Success") {
            let lista = "";
            data.comunicados.forEach((comunicado) => {
                if (comunicado.token.includes(busqueda)) {
                    if(comunicado.tipo_id.includes(tipo)){
                    if (estado) {
                        lista += `<tr class="table ${comunicado.solucionado ? 'table-success' : ''}">
                    <td>${comunicado.token}</td>
                    <td>${comunicado.tipo_id}</td>
                    <td>${comunicado.comunicante_id}</td>
                    <td>${comunicado.fecha}</td>
                    <td><a href="${comunicado.token}" class="btn btn-default ml-1"><i class="fa-regular fa-eye"></i></a></td>
                </tr>`
                    } else {
                        if (comunicado.solucionado === false) {
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
                }
            });
            cuerpoTabla.innerHTML = lista;
        } else {
            alert("Comunicados no encontrados...")
        }
    } catch (error) {
        console.log(error);
    }
}

const cargaInicial = async () => {
    await listarComunicados('', true, '');

    buscar.addEventListener("input", (event) => {
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

    solucionado.addEventListener("change", (event) => {
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