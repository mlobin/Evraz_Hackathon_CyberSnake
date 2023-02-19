import { useState, useEffect } from 'react';

import server from '../../apis/server';


export function useGraph() {
    const [graphPoints, setGraphPoints] = useState([]);
    // const [loading, setLoading] = useState(true);

    const getGraph = async () => {
        try {
          const data = await server.post('/exhauster/graph/', ["bearing_with_vibration_sensor_1__temperature"]);
          setGraphPoints(data.data);
        //   setLoading(true)
        } catch (error) {
            console.log(error);
        //   onCatchError(error, 'Cannot fetch hashtags. Try again later');
        }
      };
    
      useEffect(() => {
        setTimeout(5000)
        getGraph()
      }, [])

  return graphPoints;
}
