let buttons = document.querySelectorAll('button')

let ru = document.querySelector('#ru')
let en = document.querySelector('#en')

buttons.forEach(button=> {
   button.addEventListener('click', (e) => {
    let title = document.querySelector('.title')
    //    console.log(ru)
    //    console.log(en)
      if (e.target === ru){
        title.innerHTML = "привет"
      }
      else if (e.target === en){
         title.innerHTML = "hello"
      }
   }
 )
})

// lang.addEventListener ("click", () => {
// if (className = "ru"){
// title.textContent = "Hello"
// }
// if (className = "en"){
//     title.textContent = "hi" 
// }


// )