import { StyleSheet, Text, View } from "react-native";
import { useState, useEffect } from "react";

let object = {
  area: [],
  location: [],
  time: [],
  type: [],
}

function App() {
  const [data, setData] = useState<any | null>(null);

  useEffect(() => {

    fetch("http://localhost:5000/api")
      .then(response => response.json())
      .then(data => {
        console.log(ta);
        setData(data);
      })
  }, []);

  return (
    <View>
      <Text style={styles.mainText}>Area: </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  view: {
    backgroundColor: 'black'
  },
  mainText: {
    textAlign: 'center'
  }
})

export default App;