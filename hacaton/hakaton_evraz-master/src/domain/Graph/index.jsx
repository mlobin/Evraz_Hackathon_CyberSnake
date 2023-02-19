import React from 'react';
// import Spiner from '../../components/Spiner';
import ReactApexChart from "react-apexcharts";

import { useGraph } from './useGraph';
import {options1, options2, options3} from './services/chart_options'
import "./index.css"
// import ExhausterRow from './component/ExhausterRow';

const Graph = () => {
    const graphPoints = useGraph();
    console.log(graphPoints)
    
    // const prepared_options_2 = options2(Object.values(graphPoints))
    // const series = [{
    //           data: [34, 44, 54, 21, 12, 43, 33, 23, 66, 66, 58]
    //         }]
//   if (loading) return <Spiner isFullScreen size="large" />;
    const data1 = [{data:Object.values(graphPoints)}]
    console.log(data1);
    return (
        <div>
            <ReactApexChart options={options3} series={data1} height={500}/>
        </div>
    );
};

export default Graph;

