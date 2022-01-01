import { combineReducers } from 'redux'
import monitorReducer from "./monitor";

const rootReducer = combineReducers({
    monitorReducer,
})

export default rootReducer