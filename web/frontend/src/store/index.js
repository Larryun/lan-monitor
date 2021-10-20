import { createStore } from "vuex"
import client from "./modules/client"

export const store = createStore({
    modules: {
        client: client
    }
})