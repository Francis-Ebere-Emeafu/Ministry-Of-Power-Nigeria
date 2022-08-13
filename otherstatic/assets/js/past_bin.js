
image.addEventListener('change',()=>{
    const img_data =image.files[0]
    const url = URL.createObjectURL(img_data)
    console.log(url)
    imgBox.innerHTML = `<img src="${url}" width="100%">`
})

console.log(form)
console.log(csrf)