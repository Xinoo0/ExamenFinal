var nombre = document.getElementById('name');
var apellidoP = document.getElementById('ApellidoP');
var apellidoM = document.getElementById('ApellidoM');
var error = document.getElementById('error');
error.style.color = 'white'

document.addEventListener('input', (e) => {
    const rut = document.getElementById('rut');
  
    if (e.target === rut) {
      let rutFormateado = FormatoRut(rut.value);
      rut.value = rutFormateado;
    }
});
function subirFormulario(){
    console.log('Subiendo Formulario..... ');
    var mensajeError = [];
    var respuesta = confirm("¿Quiere enviar este formulario?")
    if(nombre.value === null || nombre.value ===''){
        mensajeError.push('Ingrese su nombre')
    };
    if(apellidoP.value === null || apellidoP.value ===''){
        mensajeError.push('Ingrese su Apellido Paterno')
    };
    if(apellidoM.value === null || apellidoM.value ===''){
        mensajeError.push('Ingrese su Apellido Materno')
    };
    if(rut.value === null || rut.value === ''){
        mensajeError.push('Ingrese su Rut')
    }
    error.innerHTML = mensajeError.join(' <br>');
    if(respuesta==true){
        return true;
    } else{
        return false
    }
};

function FormatoRut(rut) {
    const rutLimpio = rut.replace(/[^0-9kK]/g, '');

    const cuerpo = rutLimpio.slice(0, -1);
    const dv = rutLimpio.slice(-1).toUpperCase();

    if (rutLimpio.length < 2) return rutLimpio;

    let cuerpoFormatoMiles = cuerpo
        .toString()
        .split('')
        .reverse()
        .join('')
        .replace(/(?=\d*\.?)(\d{3})/g, '$1.');

    cuerpoFormatoMiles = cuerpoFormatoMiles
        .split('')
        .reverse()
        .join('')
        .replace(/^[\.]/, '');

    return `${cuerpoFormatoMiles}-${dv}`;
};
  
