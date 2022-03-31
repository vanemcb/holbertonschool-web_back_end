export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    this._name = name;

    if (typeof length !== 'number') throw TypeError('Length must be a number');
    this._length = length;

    students.forEach((student) => {
      if (typeof student !== 'string') throw TypeError('Students must be an array of strings');
    });
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('Name must be a string');
    this._name = newName;
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') throw TypeError('Length must be a number');
    this._length = newLength;
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    newStudents.forEach((student) => {
      if (typeof student !== 'string') throw TypeError('Students must be an array of strings');
    });
    this._students = newStudents;
  }
}
