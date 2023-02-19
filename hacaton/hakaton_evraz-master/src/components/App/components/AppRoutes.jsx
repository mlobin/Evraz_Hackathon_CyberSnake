import React from 'react';
import { Route, Routes } from 'react-router-dom';

import AllExhausters from '../../../domain/ExhaustersAll'
import Exhauster from '../../../domain/Exhauster'
import NotFoundPage from './NotFoundPage';
import StartingPage from '../../../domain/Landing'
import Graph from '../../../domain/Graph'


const AppRoutes = () => {
  return (
    <Routes>
      <Route path="" element={<AllExhausters/>} />
      <Route path="exhauster/:rotor_number" element={<Exhauster/>} />
      <Route path="graph/" element={<Graph/>} />
      {/* <Route path="/" element={<StartingPage/>} /> */}
      <Route path='*' element={<NotFoundPage/>} />
    </Routes>
  );
};

export default AppRoutes;
