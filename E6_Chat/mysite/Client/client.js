const btn = document.querySelector('.j-btn');
btn.addEventListener('click', () =>{
    const options = {
      method: 'GET', // выбор метода запроса
      mode: 'cors', // режим работы запроса
      headers: { // дополнительные заголовки для запроса
        'Content-Type': 'application/json',
      },
    }
//fetch('https://jsonplaceholder.typicode.com/users', options) // удаленный ресурс работает
    fetch( 'http://127.0.0.1:8000/asd/heroes/', options) // локальный ресурс  работает только
      .then((response) => { return response.json(); })
      .then((data) => { console.log(data); })
      .catch(() => { console.log('error') });

});

const btn1 = document.querySelector('.j-btn1');

btn1.addEventListener('click', () => {
  // Настраиваем наш запрос
  const options1 = {
    // Будем использовать метод POST
    method: 'POST',
    // Добавим тело запроса
    body: JSON.stringify({
    name: "Beer",
    alias: "Sweety"
    }),
    // Дополнительный заголовое с описанием типа данных,
    // которые мы отправляем серверу. В данном случае
    // сервер jsonplaceholder будет знать, как ему
    // обрабатывать запрос
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  }
  // Делаем запрос за данными
  fetch('http://127.0.0.1:8000/asd/heroes/', options1)
    .then(response => response.json())
    .then(json => console.log(json))
});

const btn2 = document.querySelector('.j-btn2');

btn2.addEventListener('click', () => {
  // Настраиваем наш запрос
  const options2 = {
    // Будем использовать метод Delete
    method: 'DELETE',

  }

fetch('http://127.0.0.1:8000/asd/heroes/12', options2)
  if (!response.ok) {
    const message = 'Error with Status Code: ' + response.status;
    console.log(message);
  }
  else {
    console.log('Delete OK!')
  }
});

var razmetka = "";

fetch( 'http://127.0.0.1:8000/asd/heroes/') // локальный ресурс  работает только
      .then((response) => { return response.json(); })
      .then((data) => { razmetka=(data); })
      .catch(() => { console.log('error') });

console.log(razmetka);

