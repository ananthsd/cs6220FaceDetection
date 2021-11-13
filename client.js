// import Blob from 'cross-blob';
// import("cross-blob").then(module => { Blob = module });
require('isomorphic-fetch');
console.log("test")
var FormData = require('form-data');
var fs = require('fs');

const formData = new FormData();
var file = fs.readFileSync("patrick.jpg")
// const fileblob = new Blob([file], { type: 'image/jpeg' });

console.log(file)
formData.append('image', file);

const stats = fs.statSync("patrick.jpg");
const fileSizeInBytes = stats.size;

fetch('http://127.0.0.1:5000/search', {
  method: 'POST',
  body: formData,
  headers: {
    'content-type': 'multipart/form-data'
  }
})
.then((response) => response)
.then((result) => {
  console.log('Success:', result);
})
.catch((error) => {
  console.error('Error:', error);
});
