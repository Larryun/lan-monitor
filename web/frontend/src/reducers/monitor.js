import {getDateOnly} from "../util";

const initialState = {
    clients: [],
    status: {},
    current_date: getDateOnly(new Date()).getTime() / 1000
}
export default function monitorReducer(state = initialState, action) {
    switch (action.type) {
        case 'monitor/loadClients': {
            return {
                ...state,
                clients: action.payload,
                status: {},
            }
        }
        case 'monitor/addClient': {
            return {
                ...state,
                clients: [
                    ...state.clients,
                    action.payload
                ]
            }
        }
        case 'monitor/setCurrentDate': {
            return {
                ...state,
                current_date: action.payload
            }
        }
        case 'monitor/setClientStatus': {
            return {
                ...state,
                status: {
                    ...state.status,
                    [action.payload.client_id]: action.payload.intervals
                }
            }
        }
        case 'monitor/removeClientStatus': {
            return {
                ...state,
                status: {}
            }
        }
        default: {
            return state
        }
    }
}