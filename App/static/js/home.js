


//注册界面
// 密码是否合法验证
$('#one').blur(function () {
    var password1 = $('#one').val()

    if (password1.length < 6 || password1.length >12)
    {

        $('#one-two').removeClass('glyphicon-ok').addClass('glyphicon-remove')
    }else
    {

        $('#one-two').removeClass('glyphicon-remove').addClass('glyphicon-ok').removeClass('bg-danger')
    }
})



// 验证两次的密码是否一致
$('#two').blur(function () {
    var password1 = $('#one').val()
    var password2 = $('#two').val()
    if (password1 == password2) {
        $('#two-one').addClass('glyphicon-ok').removeClass('glyphicon-remove')


    }else
    {
        $('#two-one').removeClass('glyphicon-ok').addClass('glyphicon-remove')

    }

})


// 有效的邮箱

var reg = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+[\.][a-zA-Z0-9_-]+$/

$('#three').blur(function () {

    var email = $('#three').val()
    if (reg.test(email)){
        console.log(email)
        $('#three-one').addClass('glyphicon-ok').removeClass('glyphicon-remove')
    }else
    {
        $('#three-one').removeClass('glyphicon-ok').addClass('glyphicon-remove')
    }

})
// 邮箱,密码不合格阻止提交

$('#submit').click(function (event) {
    var password1 = $('#one').val()
    var password2 = $('#two').val()
    var email = $('#three').val()

    if (password1.length > 6 && password1.length < 12 && password1 == password2 && reg.test(email)) {
        console.log(11111111)


    }else
    {
        console.log(0)
        event.preventDefault()

    }
})






//登录界面
//发起请求验证帐号是否存在
$('#four').blur(function () {
    var name = $('#four').val()
    data = {
        'name':name
    }
    $.get('/namecheck/',data,function (response) {
        console.log(response['users'])
        if (response['status'] == '1') {
            console.log('succed')
            $('#four-one').html('')
            $('#four-two').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        }else
        {
            console.log('fail')
            $('#four-two').addClass('glyphicon-remove').removeClass('glyphicon-ok')
            $('#four-one').html('帐号不存在')
        }

    })

})






