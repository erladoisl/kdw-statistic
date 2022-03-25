import React, { useEffect, useState } from 'react';
import UsersService from '../../../../service/UsersService';

const usersService = new UsersService();

const TotalRegistration = (props) => {
    const [statistic, setStatistic] = useState({ regs: { 0: 0 }, reg_online: { 0: 0 }, reg_offline: { 0: 0 }, speaker: { 0: 0 }, accepted_speaker: { 0: 0 }, accepted_speaker_online: { 0: 0 }, accepted_speaker_offline: { 0: 0 } });

    useEffect(() => {
        usersService.getTotalRegistrationStatistic(props.startDate, props.endDate).then(function (result) {
            setStatistic(JSON.parse(result.data));
        });
    }, [props.startDate, props.endDate]);

    return (
        <tr>
            <td>Итого:</td>
            <td>{statistic.regs[0]}</td>
            <td>{statistic.reg_online[0]}</td>
            <td>{statistic.reg_offline[0]}</td>
            <td>{statistic.speaker[0]}</td>
            <td>{statistic.accepted_speaker[0]}</td>
            <td>{statistic.accepted_speaker_online[0]}</td>
            <td>{statistic.accepted_speaker_offline[0]}</td>
        </tr>
    );
}

export default TotalRegistration;