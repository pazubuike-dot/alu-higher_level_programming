#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  // Sort unique items descending or use absolute sort to find sequence
  args.sort((a, b) => b - a);
  console.log(args[1]);
}