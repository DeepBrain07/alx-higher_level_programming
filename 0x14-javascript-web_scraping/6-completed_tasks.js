#!/usr/bin/node

const request = require('request');

const url = process.argv[2]
let myDict = {}
await request(url, (error, response, body) => {
  const data = JSON.parse(body)
  let count = 0
  for (let i = 0; i < data.length; i++) {
    for (let j = 1; j <= 7; j++) {
      if (j === data[i]["userId"]) {
        if (data[i]["completed"] == true) {
          count++;
          myDict[j.toString()] = count
        }
      }
  }
  }
  console.log(myDict)
})
