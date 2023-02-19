import { useState, useEffect } from 'react';

import server from '../../../apis/server';


export function useExhausters() {
  const [exhausters, setExhausters] = useState([]);
  const [loading, setLoading] = useState(true);

  const getExhausters = async () => {
    try {
      const data = await server.get('/exhauster/');
      setExhausters(data.data);
      setLoading(false)
    } catch (error) {
      console.log(error);
    //   onCatchError(error, 'Cannot fetch hashtags. Try again later');
    }
  };

  useEffect(() => {
    getExhausters();
  }, [exhausters]);

  return [exhausters, loading];
}
