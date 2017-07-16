$(document).ready(function () {
    var searchBar = $('#search_course');
    searchBar.on('input', function () {
        $.ajax({
            url: '/search?course=' + searchBar.val(),
            success: function (result) {
                var validCourses = JSON.parse(result['courses']);
                var courseList = $('#course_list li');
                outer: for (var i = 0; i < courseList.length; i++) {
                    for (var j = 0; j < validCourses.length; j++) {
                        if (validCourses[j].fields.name == courseList[i].children[0].innerHTML) {
                            courseList[i].style.display = '';
                            continue outer;
                        }
                    }
                    courseList[i].style.display = 'none';
                }
            }
        });
    });
});
