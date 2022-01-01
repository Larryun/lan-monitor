const initialState = {
    clients: [],
    status: []
}
export default function monitorReducer(state = initialState, action) {
    switch (action.type) {
        case 'monitor/loadClients': {
            return {
                clients: action.payload,
                status: [],
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
        default: {
            return state
        }
    }
}