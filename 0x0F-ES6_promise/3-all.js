import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  const promise1 = await uploadPhoto().catch(() => console.log('Signup system offline'));
  const promise2 = await createUser().catch(() => console.log('Signup system offline'));
  console.log(`${promise1.body} ${promise2.firstName} ${promise2.lastName}`);
}
