import Registration from './Registration/Registration';
import DatePicker from "react-datepicker";
import React, { useState } from 'react';
import "react-datepicker/dist/react-datepicker.css";
import Location from './Location/Location';
import TwoYearsStatistic from './Registration/TwoYearsStatistic/TwoYearsStatistic';
import BtnScrollUp from './BtnScrollUpp/BtnScrollUp';


const Statistic = () => {
    let [startDate, setStartDate] = useState(new Date(new Date().setUTCFullYear(new Date().getFullYear() - 1)));
    let [endDate, setEndDate] = useState(new Date());

    const startDateChange = (date) => {
        setStartDate(date);
    }

    const endDateChange = (date) => {
        setEndDate(date);
    }

    return (
        <div id="container" className='container'>
            <h2 className=" heading_level-3 mt-5 ">Период:</h2>
            <div className='row m-4'>
                <div className='col-3'>
                    <label htmlFor="basic-url" className="form-label">Стартовая дата:</label>
                    <DatePicker
                        selected={startDate}
                        onChange={startDateChange}
                        name="startDate"
                        className='col-3 form-control'
                        dateFormat="Y-M-d"
                    />
                </div>
                <div className='col-3'>
                    <label htmlFor="basic-url" className="form-label">Конечная дата:</label>
                    <DatePicker
                        selected={endDate}
                        onChange={endDateChange}
                        name="endDate"
                        className='col-3 form-control'
                        dateFormat="Y-M-d"
                    />
                </div>
            </div>
            <div className='row  m-4'>
                {/* <div className='col-3'>
                    <button className="btn btn-primary m-1" onClick={this.savePeriod}>Сохранить период</button>
                </div> */}
            </div>
            <Registration startDate={startDate.toISOString().slice(0, 10)} endDate={endDate.toISOString().slice(0, 10)} />
            <Location startDate={startDate.toISOString().slice(0, 10)} endDate={endDate.toISOString().slice(0, 10)} />
            <TwoYearsStatistic />
            <BtnScrollUp />
        </div>
    )
}

export default Statistic;