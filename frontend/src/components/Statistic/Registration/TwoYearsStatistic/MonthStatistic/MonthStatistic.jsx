import { useEffect } from 'react';
import { useState } from 'react';
import UsersService from '../../../../../service/UsersService';
import Chart from 'react-apexcharts'

const usersService = new UsersService();

const MonthStatistic = (props) => {
    const [statistic, setStatistic] = useState({});


    const updateStatistic = () => {
        usersService.getMonthsStatistic().then(function (result) {
            setStatistic(result.data);
        });
    };

    useEffect(() => {
        updateStatistic();
    }, [props.startDate, props.endDate]);

    if (Object.keys(statistic).length > 0) {
        const options = {
            chart: {
                id: "basic-bar"
            },
            xaxis: {
                categories: statistic['months']
            }
        }
        const series = [
            {
                name: "2021",
                data: statistic['2021']
            },
            {
                name: "2022",
                data: statistic['2022']
            }
        ]

        return (
            <div>
                <div className='row'>
                    <div className='col-6 m-auto'>
                        <div className="center-block">
                            <Chart
                                options={options}
                                series={series}
                                type="line"
                                width="100%"
                            />
                        </div>
                    </div>
                </div>
            </div >
        )
    }
    return <></>
}

export default MonthStatistic;