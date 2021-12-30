import axios from 'axios';

let api_url = process.env["REACT_APP_API_URL"]

function getClients() {
    return axios.get(api_url + "/client")
}

function getClientStatus(client_id, limit) {
    return axios.get(api_url + `/client/status/${client_id}?limit=${limit}`)
}

export { getClients, getClientStatus }