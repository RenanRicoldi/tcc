import * as React from 'react';
import * as WebBrowser from 'expo-web-browser';
import { makeRedirectUri, useAuthRequest } from 'expo-auth-session';
import { Button } from 'react-native';
import { useAuth } from '../../context/auth';

WebBrowser.maybeCompleteAuthSession();

const discovery = {
  authorizationEndpoint: 'https://www.strava.com/oauth/mobile/authorize',
  tokenEndpoint: 'https://www.strava.com/oauth/token',
  revocationEndpoint: 'https://www.strava.com/oauth/deauthorize',
};

const StravaAuthButton: React.FC = () => {
  const { setAuth } = useAuth();

  const [request, response, promptAsync] = useAuthRequest(
    {
      clientId: '72497',
      scopes: ['activity:read_all'],
      redirectUri: makeRedirectUri({
        useProxy: false,
      }),
    },
    discovery,
  );

  React.useEffect(() => {
    if (response?.type === 'success') {
      const { code } = response.params;
      setAuth({
        logged: true,
        accessCode: code,
      });
    } else {
      console.log(`uri: ${makeRedirectUri({ useProxy: false })}`);
      setAuth({
        logged: false,
        accessCode: '',
        error: 'Não foi possível acessar sua conta',
      });
    }
  }, [response, setAuth]);

  return (
    <Button
      disabled={!request}
      title="Login"
      color="#ff7000"
      onPress={() => {
        promptAsync();
      }}
    />
  );
};

export default StravaAuthButton;
