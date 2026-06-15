import { Text, View } from "react-native";
import { useEffect } from "react";

function App() {
  const fetchAPI = async () => {
    const url = "http://localhost:5000/api";
    const response = await fetch(url);
    const data = await response.json();

    console.log(data);
  }

  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text>Edit app/index.tsx to edit this screen.</Text>
    </View>
  );
}

export default App;