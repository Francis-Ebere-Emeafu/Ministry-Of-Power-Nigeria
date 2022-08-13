console.log('Hello Ifunanyachukwu')

const form = document.getElementById('login-form')
const username = document.getElementById('id_username')
const password = document.getElementById('id_password')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


form.addEventListener('submit', e=>{
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('username', username.value)
    fd.append('password', password.value)

    $.ajax({
        type: "POST",
        url: "accounts/login/",
        // form.attr("action"),
        // "{% url 'login' %}",
        enctype: "multipart/form-data",
        data: fd,

        success: function(response){
            console.log(response)
            
            window.location = "{% url 'profile' %}"
            
        },
        error: function(error){
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})