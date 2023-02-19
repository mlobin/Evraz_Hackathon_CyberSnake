import { useState, useEffect } from 'react';

import server from '../../../apis/server';


export function useExhauster() {
  const [exhauster, setExhauster] = useState([]);
  const [loading, setLoading] = useState(true);

  const getExhauster = async () => {
    try {
      const exhauster_number = window.location.href.split("/").slice(-1)[0];
      console.log(exhauster_number)
      const data = await server.get('/exhauster/one/'+String(exhauster_number));
      setExhauster(data.data);
      setLoading(false)
    } catch (error) {
        console.log(error);
    //   onCatchError(error, 'Cannot fetch hashtags. Try again later');
    }
  };

  useEffect(() => {
    getExhauster();
  }, [exhauster]); 

  return [exhauster, loading];
}
