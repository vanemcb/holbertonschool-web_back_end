export default function getStudentIdsSum(listEstudents) {
  return listEstudents.reduce((prev, current) => prev + current.id, 0);
}
