import React, { useEffect, useState } from 'react';
import UsersService from '../../../service/UsersService';
import ReactApexChart from "react-apexcharts"

const usersService = new UsersService();

const Location = (props) => {
    const [series, setSeries] = useState([0, 0, 0])

    let options = {
        chart: {
            width: 380,
            type: 'pie',
        },
        labels: ['Мир', 'Татарстан', 'Россия'],
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    }

    useEffect(() => {
        usersService.getLocationStatistic(props.startDate, props.endDate, 0).then(function (result) {
            const resJson = JSON.parse(result.data)
            setSeries(Object.keys(resJson).map((key) => { return resJson[key]['0'] }))
        })
    }, [props.startDate, props.endDate])


    if (series.reduce((prev, el) => prev + el, 0) > 0)
        return (
            <div className='row' >
                <h2 className=" heading_level-3 mt-5 ">Статистика регистраций по местоположению</h2>
                <ReactApexChart
                    options={options} series={series} type="pie" width={500}
                />
            </div >
        )

    return (
        <div className='row' ></div>
    )
}

export default Location; 