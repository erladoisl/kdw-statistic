import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default class UsersService {

	constructor() { }

	getRegistrationStatistic(startDate, endDate, page_num) {
		let data = [];
		const url = `${API_URL}/api/statistic/users/registrations/count/in-days/by-period?startDate=${startDate}&endDate=${endDate}&page_num=${page_num}`;

		return axios.get(url).then(response => {
			data = response.data;
		}).catch(error => {
			console.log(`error while getting registration statistic from ${startDate} to ${endDate}: ${error}`);
		}).then(() => {
			return data;
		});
	}

	getTotalRegistrationStatistic(startDate, endDate) {
		let data = [];
		const url = `${API_URL}/api/statistic/users/registrations/count/total/by-period?startDate=${startDate}&endDate=${endDate}`;

		return axios.get(url).then(response => {
			data = response.data;
		}).catch(error => {
			console.log(`error while getting total registration count from ${startDate} to ${endDate}: ${error}`);
		}).then(() => {
			return data;
		});
	}

	getLocationStatistic(startDate, endDate) {
		let data = [];
		const url = `${API_URL}/api/statistic/users/registrations/locations/by-period?startDate=${startDate}&endDate=${endDate}`;

		return axios.get(url).then(response => {
			data = response.data;
		}).catch(error => {
			console.log(`error while getting total location count from ${startDate} to ${endDate}: ${error}`);
		}).then(() => {
			return data;
		});
	}

	getMonthsStatistic() {
		let data = [];
		const url = `${API_URL}/api/statistic/users/registrations/count/by-months`;

		return axios.get(url).then(response => {
			data = response.data;
		}).catch(error => {
			console.log(`error while getting registrations count per month: ${error}`);
		}).then(() => {
			return data;
		});
	}
}