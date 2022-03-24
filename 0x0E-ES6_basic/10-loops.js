export default function appendToEachArrayValue(array, appendString) {
  let idx = 0
  for (let item of array) {
    array[idx] = appendString + item;
    idx++
  }

  return array;
}
