import { useEffect } from 'react';
import { useState } from 'react';
import UsersService from '../../../service/UsersService';
import TotalRegistration from './TotalRegistration/TotalRegistration';

const usersService = new UsersService();

const Registration = (props) => {
    const [pageNum, setPageNum] = useState(0);
    const [statistic, setStatistic] = useState({ date: {} });
    const [loading, setLoading] = useState(true);

    const updateStatistic = () => {
        usersService.getRegistrationStatistic(props.startDate, props.endDate, pageNum).then(function (result) {
            setStatistic(JSON.parse(result.data));
            setLoading(false)
        });
    };

    useEffect(() => {
        setPageNum(0);
        updateStatistic();
    }, [props.startDate, props.endDate]);

    useEffect(() => {
        updateStatistic();
    }, [pageNum]);

    const nextPageHandler = () => {
        setPageNum(pageNum + 1);
    };

    const prevPageHandler = () => {
        if (pageNum > 0) {
            setPageNum(pageNum - 1);
        };
    };

    if (loading)
        return (
            <div className="numbers">
                <h2 className=" heading_level-3 mt-5 ">Загрузка данных...</h2>
            </div>
        )

    if (Object.keys(statistic.date).length > 0 || pageNum > 0)
        return (
            <div className="numbers">
                <h2 className=" heading_level-3 mt-5 ">Статистика регистраций по дням</h2>
                <div className="customers--list">
                    <table className="table">
                        <thead key="thead">
                            <tr>
                                <th>Дата</th>
                                <th>участники</th>
                                <th>online</th>
                                <th>offline</th>
                                <th>Спикеры</th>
                                <th>Подтвержденные</th>
                                <th>online</th>
                                <th>offline</th>
                            </tr>
                        </thead>
                        <tbody>
                            {Object.keys(statistic.date).map(key =>
                                <tr key={key}>
                                    <td>{statistic.date[key]}</td>
                                    <td>{statistic.regs[key]}</td>
                                    <td>{statistic.reg_online[key]}</td>
                                    <td>{statistic.reg_offline[key]}</td>
                                    <td>{statistic.speaker[key]}</td>
                                    <td>{statistic.accepted_speaker[key]}</td>
                                    <td>{statistic.accepted_speaker_online[key]}</td>
                                    <td>{statistic.accepted_speaker_offline[key]}</td>

                                </tr>)}
                            <TotalRegistration startDate={props.startDate} endDate={props.endDate} />
                        </tbody>
                    </table>
                    <button className={`btn btn-primary m-1 ${pageNum === 0 ? 'disabled' : ''}`} onClick={prevPageHandler}>назад</button>
                    <button className={`btn btn-primary m-1 ${Object.keys(statistic.date).length < 10 ? 'disabled' : ''}`} onClick={nextPageHandler}>далее</button>
                </div>
            </div>
        );

    return (
        <div className="numbers">
            <h2 className=" heading_level-3 mt-5 ">За данный период времени регистраций не найдено</h2>
        </div>
    );
};

export default Registration; 