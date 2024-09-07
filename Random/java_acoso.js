document.getElementById('form-registro').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const nombreVictima = document.getElementById('nombre-victima').value;
    const nombreAgresor = document.getElementById('nombre-agresor').value;
    const descripcion = document.getElementById('descripcion').value;
    const fecha = document.getElementById('fecha').value;
    
    const caso = {
        nombreVictima,
        nombreAgresor,
        descripcion,
        fecha
    };
    
    let casosRegistrados = JSON.parse(localStorage.getItem('casos')) || [];
    casosRegistrados.push(caso);
    localStorage.setItem('casos', JSON.stringify(casosRegistrados));
    
    mostrarCasos();
    
    document.getElementById('form-registro').reset();
});

function mostrarCasos() {
    const casosRegistrados = JSON.parse(localStorage.getItem('casos')) || [];
    const listaCasos = document.getElementById('lista-casos');
    
    listaCasos.innerHTML = '';
    
    casosRegistrados.forEach(caso => {
        const casoItem = document.createElement('li');
        
        casoItem.innerHTML = `
            <strong>Nombre de la Víctima:</strong> ${caso.nombreVictima}<br>
            <strong>Nombre del Agresor:</strong> ${caso.nombreAgresor}<br>
            <strong>Descripción:</strong> ${caso.descripcion}<br>
            <strong>Fecha:</strong> ${caso.fecha}
        `;
        
        listaCasos.appendChild(casoItem);
    });
}

// Mostrar los casos al cargar la página
document.addEventListener('DOMContentLoaded', mostrarCasos);
