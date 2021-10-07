import axiod from 'https://deno.land/x/axiod@0.23.1/mod.ts';

const api = axiod.create({
  baseURL: 'https://www.strava.com/api/v3',
})

export default api