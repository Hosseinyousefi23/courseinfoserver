$(document).ready(function () {
   $('.tab button')[0].click()
});

function showQuestions(event, id) {
    $('#question_list li').css('display', 'none');
    $('.' + id).css('display', 'list-item');
    $('.tablinks').css('background-color', '#f1f1f1');
    event.target.style.backgroundColor = '#ddd';
}

