import client from '../../api/client'

// initial state
const state = () => ({
    clients: []
})

// getters
const getters = {
    getClients: (state) => {
        return state.clients
    },
}

// actions
const actions = {
    fetchClients: function({state}) {
        client.getClients().then((resp) => {
            state.clients = resp.data
        })
    }
}

// mutations
const mutations = {
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}