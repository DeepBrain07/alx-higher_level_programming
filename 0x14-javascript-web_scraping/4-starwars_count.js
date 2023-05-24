#!/usr/bin/node

const request = require('request');
let count = 0;
for (let i = 1; i <= 7; i++) {
  const id = i.toString();
  const url = process.argv[2] + '/' + id;
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    }
    const data = JSON.parse(body);
    if (data.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
    if (i === 7) {
      console.log(count);
    }
  });
}
