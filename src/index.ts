import { getActivityInfo } from './requests/activities.ts';

async function App() {
  const activityInfo = await getActivityInfo('5692356983');

  if(!activityInfo)
    return

  console.log(activityInfo.segment_efforts.map(segment => ({
    location: `${segment.name}, ${segment.segment.city}, ${segment.segment.state} - ${segment.segment.country}`,
    startPosition: {
      latitude: segment.segment.start_latitude,
      longitude: segment.segment.start_longitude
    },
    endPosition: {
      latitude: segment.segment.end_latitude,
      longitude: segment.segment.end_longitude
    },
  })))
}

App()