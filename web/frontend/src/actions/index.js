import {getClients, getClientStatus} from "../api/monitor";
import store from "../store";
import {ONE_DAY} from "../constants";

export const loadClients = (clients) => ({
    type: 'monitor/loadClients',
    payload: clients
})

export const setCurrentDate = (date) => ({
    type: 'monitor/setCurrentDate',
    payload: date
})

export const setClientStatus = (client_id, intervals) => ({
    type: 'monitor/setClientStatus',
    payload: {client_id, intervals}
})

export const removeClientStatus = () => ({
    type: 'monitor/removeClientStatus',
})

export const incrementCurrentDate = () => (dispatch, getState) => {
    dispatch(setCurrentDate(getState().monitor.current_date + ONE_DAY))
    dispatch(removeClientStatus())
    dispatch(fetchClientStatus())
}

export const decrementCurrentDate = () => (dispatch, getState) => {
    dispatch(setCurrentDate(getState().monitor.current_date - ONE_DAY))
    dispatch(removeClientStatus())
    dispatch(fetchClientStatus())
}

export const setDateAndFetchStatus = (date) => (dispatch, getState) => {
    dispatch(setCurrentDate(date))
    dispatch(removeClientStatus())
    dispatch(fetchClientStatus())
}

export const fetchClientStatus = (cb) => (dispatch, getState) => {
    let clients = getState().monitor.clients
    for (let i = 0; i < clients.length; i++) {
        // get status for each clients
        getClientStatus(
            clients[i]._id,
            getState().monitor.current_date,
            getState().monitor.current_date + 24 * 60 * 60,
            100
        ).then((res) => {
            dispatch(setClientStatus(clients[i]._id, res.data))
            // call callback at the end only
            if (typeof cb === 'function' && clients.length - 1) {
                cb()
            }
        })
    }
}

export const fetchClients = (cb) => () => {
    getClients().then((res) => {
        store.dispatch(loadClients(res.data))
        // call callback when done
        cb()
    })
}


