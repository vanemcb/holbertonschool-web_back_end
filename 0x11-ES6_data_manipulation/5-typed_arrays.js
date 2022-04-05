export default function createInt8TypedArray(length, position, value) {
  const buffer = ArrayBuffer(length);
  const typedArray = Int8Array(buffer);
}