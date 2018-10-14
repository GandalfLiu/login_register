

$.get('/jsontest/',function (response) {
    console.log(response)
    for (i = 0; i < response.length; i++) {
        var img = $("<img/>").attr('src','/static/img/'+response[i]).appendTo($('body'))
    }

})
