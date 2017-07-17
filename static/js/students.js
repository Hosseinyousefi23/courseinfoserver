$(document).ready(function () {
    var searchBar = $('#search_student');
    searchBar.on('input', function () {
        $.ajax({
            url: '/search?student=' + searchBar.val(),
            success: function (result) {
                var validStudents = JSON.parse(result['students']);
                console.log(validStudents);
                var studentList = $('#student_list li');
                outer: for (var i = 0; i < studentList.length; i++) {
                    for (var j = 0; j < validStudents.length; j++) {
                        if (validStudents[j].fields.first_name + ' ' + validStudents[j].fields.last_name == studentList[i].children[0].innerHTML) {
                            studentList[i].style.display = '';
                            continue outer;
                        }
                    }
                    studentList[i].style.display = 'none';
                }
            }
        });
    });
});
