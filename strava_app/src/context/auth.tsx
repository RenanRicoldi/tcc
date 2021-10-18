import * as React from 'react';

interface IData {
  accessCode: string;
  logged: boolean;
  error?: string;
}

interface IContext extends IData {
  setAuth: React.Dispatch<React.SetStateAction<IData>>;
}

const AuthContext = React.createContext<IContext>({} as IContext);

const AuthProvider: React.FC = ({ children }) => {
  const [auth, setAuth] = React.useState({
    accessCode: '',
    logged: false,
  });

  return (
    <AuthContext.Provider value={{ ...auth, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
};

function useAuth() {
  const context = React.useContext(AuthContext);

  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider.');
  }

  return context;
}

export { AuthProvider, useAuth };
