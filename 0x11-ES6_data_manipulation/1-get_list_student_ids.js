export default function getListStudentIds(array) {
  if (!Array.isArray(array)) return [];
  const listIds = array.map((item) => item.id);
  return listIds;
}
