$(document).ready(function () {
    var searchBar = $('#search_prof');
    searchBar.on('input', function () {
        $.ajax({
            url: '/search?prof=' + searchBar.val(),
            success: function (result) {
                var validProfs = JSON.parse(result['profs']);
                var profList = $('#prof_list li');
                outer: for (var i = 0; i < profList.length; i++) {
                    for (var j = 0; j < validProfs.length; j++) {
                        if (validProfs[j].fields.first_name + ' ' + validProfs[j].fields.last_name == profList[i].children[0].innerHTML) {
                            profList[i].style.display = '';
                            continue outer;
                        }
                    }
                    profList[i].style.display = 'none';
                }
            }
        });
    });
});

