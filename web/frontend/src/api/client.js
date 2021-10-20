import axios from "axios"

var BASE_URL = "http://127.0.0.1:5000"

export default {
    getClients() {
        return axios.get(BASE_URL + "/client")
    },
    getClientStatus(client_id) {
        return axios.get(BASE_URL + "/client/status/" + client_id)
    }
}