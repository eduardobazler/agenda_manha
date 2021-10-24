$(document).ready(function (){

    var deleteBtn = $('.delete-btn-tarefa');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var dellink = $(this).attr('href');
        var result = confirm('Tem certeza que quer deletar esta tarefa?')

        if(result) {
            window.location.href = dellink;
        }

    });

});

$(document).ready(function (){

    var deleteBtn = $('.delete-btn-afirmacao');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var dellink = $(this).attr('href');
        var result = confirm('Tem certeza que quer deletar esta afrimação?')

        if(result) {
            window.location.href = dellink;
        }

    });

});

$(document).ready(function (){

    var deleteBtn = $('.delete-btn-entrada');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var dellink = $(this).attr('href');
        var result = confirm('Tem certeza que quer deletar esta entrada?')

        if(result) {
            window.location.href = dellink;
        }

    });

});
