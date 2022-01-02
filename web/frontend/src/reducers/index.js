import { combineReducers } from 'redux'
import monitorReducer from "./monitor";

const rootReducer = combineReducers({
    monitor: monitorReducer,
})

export default rootReducer