import "react-datepicker/dist/react-datepicker.css";
import MonthStatistic from './MonthStatistic/MonthStatistic';


const TwoYearsStatistic = () => {

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
                            <th>Всего участников</th>
                            <th>Спикеры</th>
                            <th>Всего участников</th>
                            <th>Спикеры</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>15302</td>
                            <td>620</td>
                            <td>100(-99.34)</td>
                            <td>3(-96)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <br />
        </div>
    )
}

export default TwoYearsStatistic;