const inputString = "[Hello], [World], [OpenAI]";
const regex = /\[([^\]]+)\]/g;
const extractedStrings = [];
let match;

while ((match = regex.exec(inputString))) {
  extractedStrings.push(match[1]);
}

console.log(typeof extractedStrings);
