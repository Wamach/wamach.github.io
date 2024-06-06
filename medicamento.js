let medicamentos = [];

document.getElementById('medicamentosForm').addEventListener('submit', function(e) {
  e.preventDefault();

  let inicioStr = document.getElementById('inicio').value;
  let nombreMedicamento = document.getElementById('nombre').value;
  let frecuenciaStr = document.getElementById('frecuencia').value;
  let duracionStr = document.getElementById('duracion').value;

  let inicioMedicamento = new Date(inicioStr);
  let frecuenciaConsumoHoras = parseInt(frecuenciaStr);
  let duracionDias = parseInt(duracionStr);

  medicamentos.push({
    inicioMedicamento,
    nombreMedicamento,
    frecuenciaConsumoHoras,
    duracionDias
  });

  console.log(medicamentos);
});
