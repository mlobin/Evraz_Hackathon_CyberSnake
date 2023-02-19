import React from 'react';
import Spiner from '../../components/Spiner';

import { useExhausters } from './hooks/useExhausters';
import ExhausterRow from './component/ExhausterRow';

const AllExhausters = () => {
  const [exhausters, loading] = useExhausters();
  if (loading) return <Spiner isFullScreen size="large" />;
  return (
    <div >
      <div>
        {exhausters.map((exhauster) => (<ExhausterRow exhauster={exhauster}/>))}
        
      </div>
    </div>
  );
};

export default AllExhausters;
