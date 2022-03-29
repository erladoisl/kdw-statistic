import "react-datepicker/dist/react-datepicker.css";
import UsersService from '../../../../service/UsersService';
import { useEffect } from 'react';
import { useState } from 'react';
import MonthStatistic from './MonthStatistic/MonthStatistic';

const usersService = new UsersService();

const TwoYearsStatistic = (props) => {
    const [statistic, setStatistic] = useState({});

    const updateStatistic = () => {
        usersService.getTwoYearsStatistic().then(function (result) {
            setStatistic(result.data);
        });
    };

    useEffect(() => {
        updateStatistic();
    }, [props.startDate, props.endDate]);

    if (Object.values(statistic).reduce((a, b) => a + b, 0) > 0) {
        return (
            <div id="container" className='container'>
                <div className='row'>
                    <h2 className=" heading_level-3 mt-5">Статистика регистраций за последние два года</h2>
                </div>
                <MonthStatistic />
                <br />
                <div className='row'>
                    <div className="col-6 px-0">
                        <h2 className=" heading_level-2 mt-5 text-center">2021</h2>
                    </div>
                    <div className="col-6 px-0">
                        <h2 className=" heading_level-2 mt-5 text-center">2022</h2>
                    </div>
                </div>
                <div className="customers--list">
                    <table className="table">
                        <thead key="thead">
                            <tr>
                                {Object.keys(statistic).map((key, index) => {
                                    return <th key = {index}>{key}</th>
                                })}
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                {Object.values(statistic).map((value, index) => {
                                    return <th key = {index}>{value}</th>
                                })}
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br />
            </div>
        )
    }

    return <></>
}

export default TwoYearsStatistic;