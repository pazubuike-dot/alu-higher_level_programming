#!/usr/bin/node
const parsedInt = parseInt(process.argv[2], 10);

if (isNaN(parsedInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedInt}`);
}