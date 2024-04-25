const listarComunicados=async()=>{
try{
    const response = await fetch('/gestion/listar/');
    const data = await response.json();
    if(data.message === "Success"){
        let lista = "";
        data.comunicados.forEach((comunicado) => {
            lista += `<tr class="table ${ comunicado.solucionado ? 'table-success' : ''}">
                <td>${comunicado.token}</td>
                <td>${comunicado.tipo_id}</td>
                <td>${comunicado.comunicante_id}</td>
                <td>${comunicado.fecha}</td>
                <td><a href="${comunicado.token}" class="btn btn-default ml-1"><i class="fa-regular fa-eye"></i></a></td>
            </tr>`
        });
        cuerpoTabla.innerHTML= lista;
    }else{
        alert("Comunicados no encontrados...")
    }
}catch (error){
    console.log(error);
}
}

const cargaInicial=async()=>{
    await listarComunicados();
};

window.addEventListener("load", async () =>{
    await cargaInicial();
})