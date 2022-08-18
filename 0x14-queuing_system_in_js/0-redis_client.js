import { createClient } from 'redis';

(async () => {
  const client = createClient();

  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

  await client.connect();

  await client.set('key', 'value');
  const value = await client.get('key');
})();