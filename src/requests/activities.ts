import api from '../api.ts';
import { getAccessToken } from '../requests/auth.ts';

export interface IGetActivityInfo {
  'distance': number;
  'moving_time': number;
  'elapsed_time': number;
  'total_elevation_gain': number;
  'type': string;
  'id': number;
  'start_date': Date;
  'start_date_local': Date;
  'start_latitude': number;
  'start_longitude': number;
  'average_speed': number;
  'max_speed': number;
  'elev_high': number;
  'elev_low': number;
  'calories': number;
  'segment_efforts': [
    {
      'id': number;
      'name': string;
      'elapsed_time': number;
      'moving_time': number;
      'start_date': Date;
      'start_date_local': Date;
      'distance': number;
      'segment': {
        'activity_type': string;
        'elevation_high': number;
        'elevation_low': number;
        'start_latitude': number;
        'start_longitude': number;
        'end_latitude': number;
        'end_longitude': number;
        'city': string;
        'state': string;
        'country': string;
      }
    }
  ];
}

export async function getActivityInfo(activityId: string): Promise<IGetActivityInfo | null> {
  try {
    const accessToken = await getAccessToken();

    if(!accessToken)
      throw new Error('Sem token de acesso')

    const response = await api.get(`activities/${activityId}`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
      params: {
        include_all_efforts: true
      }
    })

    return response.data;
  } catch(error) {
    console.log(error);
    return null;
  }
}