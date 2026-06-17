import React, { useState, useEffect } from 'react'
import { ScrollView, View, Text, StyleSheet } from 'react-native';

export default function App() {

  let [area, setArea] = useState<any>("Loading...");
  let [time, setTime] = useState<any>("Loading...");
  let [location, setLocation] = useState<any>("Loading...");
  let [type, setType] = useState<any>("Loading...");

  useEffect(() => {
    async function fetchAPI() {
      const request = await fetch("http://localhost:5000/")
        .then((request => request.json()))
        .then((response) => {
          setArea(response?.area);
          setTime(response?.time);
          setLocation(response?.location);
          setType(response?.type);

          console.log(response);
        })
        .catch(err => console.log(err))

      return request;
    }

    fetchAPI();

  }, [])


  return (
    <ScrollView>

      <Text style={styles.text}>Area: {area}</Text>
      <Text style={styles.text}>Time: {time}</Text>
      <Text style={styles.text}>Location: {location}</Text>
      <Text style={styles.text}>Type: {type}</Text>

    </ScrollView>
  );
}

const styles = StyleSheet.create({
  text: {
    textAlign: "center",
    margin: "5%",
    fontSize: 50
  }
})