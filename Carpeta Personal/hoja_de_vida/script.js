function downloadPDF(){

    const element = document.querySelector('#pdf-content');
    /* console.log(element); */
   
    const opt = {
        margin : [ 0, 0, 0, 0], /* [ arriba , izquierda , abajo , derecha ] en mm */
        filename: 'hoja_de_vida_Jacobo_Correa.pdf',
        image: { type : 'jpeg', quality: 0.98},
        html2canvas:{
            scale:2,
            useCORS: true,
            scrollY:0,
           
        },
        jsPDF:{
            unit:"mm",
            format:"a4",
            orientation:"portrait", //  Orientacion vertical
        },
    };
    html2pdf().set(opt).from(element).save();
}

