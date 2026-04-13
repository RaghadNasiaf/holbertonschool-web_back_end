const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').filter((line) => line.length > 0);
      const studentLines = lines.slice(1);
      
      let response = `Number of students: ${studentLines.length}`;

      const fields = {};
      studentLines.forEach((line) => {
        const student = line.split(',');
        if (student.length === 4) {
          const firstName = student[0];
          const field = student[3];
          if (!fields[field]) fields[field] = [];
          fields[field].push(firstName);
        }
      });

      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const fieldLog = `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
          response += `\n${fieldLog}`;
        }
      }
      resolve(response);
    });
  });
}

module.exports = countStudents;
