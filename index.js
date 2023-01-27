// fetch('https://jsonplaceholder.typicode.com/posts')
//       .then(response => response.json())
//       .then((json)=>{
//         for (let iterator of json) {
//             html = '';
//             html += '<tr>';
//             html += '<td><h3>'+iterator.id+'</h3></td>';
//             html += '<td><h3>'+iterator.title+'</h3></td>';
//             html += '</tr>';
//             document.querySelector('#my-table tbody').innerHTML += html;
//         }
//       })

// const my_data = document.querySelector('#my-table')


// const data = { title: 'this is my first title' };

// fetch('http://127.0.0.1:8000/create_post/', {
//   method: 'POST', // or 'PUT'
//   headers: {
//     'Content-Type': 'application/json',
//   },
//   body: JSON.stringify(data),
// })
//   .then((response) => response.json())
//   .then((data) => {
//     console.log('Success:', data);
//   })
//   .catch((error) => {
//     console.error('Error:', error);
//   });