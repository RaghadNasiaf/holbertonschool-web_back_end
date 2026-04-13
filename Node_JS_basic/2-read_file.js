const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }
  if (!fs.statSync(path).isFile()) {
    throw new Error('Cannot load the database');
  }
  const data = fs.readFileSync(path, 'utf-8');
  const lines = data.trim().split('\n');
  const fields = {};
  let length = 0;

  for (let i = 1; i < lines.length; i += 1) {
    if (lines[i]) {
      length += 1;
      const field = lines[i].split(',');
      if (!fields[field[3]]) fields[field[3]] = [];
      fields[field[3]].push(field[0]);
    }
  }

  console.log(`Number of students: ${length}`);
  for (const key in fields) {
    if (Object.prototype.hasOwnProperty.call(fields, key)) {
      console.log(`Number of students in ${key}: ${fields[key].length}. List: ${fields[key].join(', ')}`);
    }
  }
}

module.exports = countStudents;
