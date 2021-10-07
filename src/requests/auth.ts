import { config } from 'https://deno.land/x/dotenv@v3.0.0/mod.ts';

import api from '../api.ts';

export async function getAccessToken(): Promise<string | null> {
  try {
    const response = await api.post('/oauth/token', {}, {
      params: {
        client_id: config({path: '.env'}).CLIENT_ID,
        client_secret: config({path: '.env'}).CLIENT_SECRET,
        refresh_token: config({path: '.env'}).REFRESH_TOKEN,
        grant_type: 'refresh_token',
      }
    })

    if(!response.data.access_token)
      throw new Error('Token não retornado')
  
    return response.data.access_token;
  } catch(error) {
    console.log(error);
    return null;
  }
}