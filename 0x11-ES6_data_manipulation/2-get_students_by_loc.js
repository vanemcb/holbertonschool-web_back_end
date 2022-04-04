export default function getStudentsByLocation(listEstudents, city) {
  return listEstudents.filter((student) => student.location === city);
}
