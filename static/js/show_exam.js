function savePDF(event) {
    var doc = new jsPDF();
    var specialElementHandlers = {
        '#editor': function (element, renderer) {
            return true;
        }
    };
    doc.addHTML($('#question_container'), 0, 12,
        function () {
            doc.save('exam.pdf');
        }
    )
    ;

}