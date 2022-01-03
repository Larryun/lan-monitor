import axios from 'axios';

let api_url = process.env["REACT_APP_API_URL"]

function getClients() {
    return axios.get(api_url + "/client")
}

function getClientStatus(client_id, start_time, end_time, interval, limit = 0) {
    return axios.get(api_url + `/client/status/${client_id}`, {
        params: {
            "start_time": start_time,
            "end_time": end_time,
            "interval": interval,
            "limit": limit
        }
    })
}

export {getClients, getClientStatus}