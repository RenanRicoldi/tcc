import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Image, StyleSheet, Text, View } from 'react-native';
import StravaAuthButton from './components/StravaAuthButton';
import { useAuth, AuthProvider } from './context/auth';

const styles = StyleSheet.create({
  container: {
    flex: 5,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  imageContainer: {
    flex: 1,
    alignItems: 'center',
    paddingTop: 50,
  },
  stravaLogo: {
    width: 240,
    height: 48,
  },
});

export default function App() {
  const { error } = useAuth();
  return (
    <AuthProvider>
      <StatusBar backgroundColor="#ff7000" />
      <View style={styles.imageContainer}>
        <Image
          style={styles.stravaLogo}
          source={{
            uri: 'https://logodownload.org/wp-content/uploads/2020/06/strava-logo-4.png',
          }}
        />
      </View>
      <View style={styles.container}>
        {!!error && <Text>{error}</Text>}
        <Text>Clique no botão para logar no App</Text>
        <StravaAuthButton />
      </View>
    </AuthProvider>
  );
}
